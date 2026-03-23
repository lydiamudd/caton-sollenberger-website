import csv

# -------------------------------------------------------
# generate_music.py
# Reads albums.csv and updates the music table in music.html
# Usage: python3 generate_music.py
# -------------------------------------------------------

APPLE_MUSIC_ICON = "https://toolbox.marketingtools.apple.com/api/v2/badges/app-icon-music/standard/en-us"
SPOTIFY_ICON = "images/spotify-icon.svg"

def build_table_row(title, artist, apple_url, spotify_url):
    """Build one <tr> block for a single album."""
    return f"""    <tr>
        <td>
            <div class="album-info">
                <span class="album-title">{title}</span><br>
                <span class="artist-name">{artist}</span>
            </div>
        </td>
        <td>
            <a href="{apple_url}" target="_blank" style="display: inline-block;">
                <img src="{APPLE_MUSIC_ICON}" alt="Listen on Apple Music" width="50" height="50" style="object-fit: contain;">
            </a>
        </td>
        <td>
            <a href="{spotify_url}" target="_blank">
                <img src="{SPOTIFY_ICON}" alt="Spotify" width="50">
            </a>
        </td>
    </tr>"""

def generate_table_rows():
    """Read albums.csv and return all table rows as a string."""
    rows = []
    with open("albums.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for album in reader:
            row = build_table_row(
                title=album["title"],
                artist=album["artist"],
                apple_music_url=album["apple_music_url"],
                spotify_url=album["spotify_url"]
            )
            rows.append(row)
    return "\n".join(rows)

def update_music_html():
    """Read music.html, replace the table body content, and save it."""

    # Read the current music.html
    with open("music.html", "r", encoding="utf-8") as f:
        html = f.read()

    # Generate fresh table rows from the CSV
    new_rows = generate_table_rows()

    # Find the markers and replace everything between them
    start_marker = "<!-- ALBUMS START -->"
    end_marker = "<!-- ALBUMS END -->"

    start_index = html.find(start_marker)
    end_index = html.find(end_marker)

    if start_index == -1 or end_index == -1:
        print("❌ Error: Could not find <!-- ALBUMS START --> and <!-- ALBUMS END --> in music.html")
        print("   Make sure you've added those comments to music.html first!")
        return

    # Build the new html with fresh rows between the markers
    new_html = (
        html[:start_index + len(start_marker)]
        + "\n"
        + new_rows
        + "\n"
        + html[end_index:]
    )

    # Save the updated music.html
    with open("music.html", "w", encoding="utf-8") as f:
        f.write(new_html)

    print("✅ music.html updated successfully!")
    print(f"   {new_rows.count('<tr>')} albums written to the table.")

# Run the script
update_music_html()