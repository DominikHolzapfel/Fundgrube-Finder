import requests
import json
from rich import print

targets = {
    'Saturn': {'id': '602faa04976e373c147b23c9', 'tid': '602faa04976e373c147b23c8',
               'stores': [
                   {'id': '310', 'name': 'Köln City (Hohe Straße)'},
                   {'id': '301', 'name': 'Köln Hansaring'},
                   {'id': '323', 'name': 'Köln Porz'},
                   {'id': '319', 'name': 'Köln Weiden'},
                   {'id': '318', 'name': 'Hürth'},
                   {'id': '215', 'name': 'Euskirchen'},
                   {'id': '783', 'name': 'Kerpen'},
               ]},
    'MediaMarkt': {'id': '602fa9fa976e370a147b23ca', 'tid': '602fa9fa976e370a147b23c9',
                   'stores': [
                       {'id': '539', 'name': 'Köln City am Dom'},
                       {'id': '620', 'name': 'Köln Chorweiler (im City Center)'},
                       {'id': '257', 'name': 'Köln Kalk (Arkaden)'},
                       {'id': '474', 'name': 'Köln Marsdorf'},
                       {'id': '1826', 'name': 'Bornheim'},
                       {'id': '1309', 'name': 'Bonn'},
                   ]}
}

looking_for = [
    'Sony Alpha 5000',
    'Sony Alpha 5100',
    'Sony Alpha 6000',
    'Sony Alpha 6100',
    'Sigma 1.4 Sony',
    'Canon EOS M200',
]


def search_store(brand, store):
    print(f"[bold blue]Searching {brand} {store['name']}[/bold blue]")

    base_url = 'https://squarelovin.com/api/index/get-stream-media/?per_call=1000&page=1&intst=gallery' \
               '&full_display_width=1628&display_width=0&show_images=4&ca=1&pi=1 '

    r = requests.get(f"{base_url}&id={targets[brand]['id']}&tid={targets[brand]['tid']}&tc={store['id']}")
    if r.status_code == 200:
        j = json.loads(r.text[9:-2])    # assumes &callback= is missing, which leads to callback=callback
        items = j['data']
        print(f"  Parsing {len(items)} items.")
        for i in items:
            if len(i['products']) == 0 or 'name' not in i['products'][0]:
                print("  [red]1 product without information[/red]")
            else:
                for lf in looking_for:
                    p_name = i['products'][0]['name'].lower()
                    lf = lf.lower()
                    if all(sub in p_name for sub in lf.split()):
                        print("   [green]Found something:[/green]")
                        print_product(i)
    else:
        print("Something went wrong :(")


def print_product(item):
    print(f"    {item['products'][0]['name']}")
    info = item['caption']['text'].split("\n")
    print(f"     {info[-3]}€ ([s]{info[-2]}€[/s] [red]-{info[-1]}%[/red])")


if __name__ == '__main__':
    for brand in targets:
        for store in targets[brand]['stores']:
            search_store(brand, store)
