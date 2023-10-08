from mwrogue.esports_client import EsportsClient
import urllib.request


def get_filename_url_to_open(site: EsportsClient, filename, team, width=None):
    response = site.client.api(
        action="query",
        format="json",
        titles=f"File:{filename}",
        prop="imageinfo",
        iiprop="url",
        iiurlwidth=width,
    )

    print(response)
    image_info = next(iter(response["query"]["pages"].values()))["imageinfo"][0]

    if width:
        url = image_info["thumburl"]
    else:
        url = image_info["url"]

    print(url)

    #In case you would like to save the image in a specific location, you can add the path after 'url,' in the line below.
    urllib.request.urlretrieve(url, f"icons/{team}.png")


teams = ["G2 Arctic"]

site = EsportsClient("lol")
for team in teams:
    response = site.cargo_client.query(
        tables="Teams=T",
        fields="T.Name, T.Short",
        where=f"(T.Short = '{team}' OR T.Name = '{team}') AND T.IsDisbanded = 'No'",
    )
    team_name = response[0]["Name"]
    url = f"{team_name}logo square.png"
    try:
        get_filename_url_to_open(site, url, team)
    except:
        ...