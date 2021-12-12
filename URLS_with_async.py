from urllib.request import Request, urlopen
import concurrent.futures

links = open('res.txt', encoding='utf8').read().split('\n')


def get_code(url):
            request = Request(
                url,
                headers={'User-Agent': 'Mozilla/5.0 (Windows NT 9.0; Win65; x64; rv:97.0) Gecko/20105107 Firefox/92.0'},
            )
            resp = urlopen(request,timeout=5)
            resp.close()


with concurrent.futures.ThreadPoolExecutor(max_workers=1000) as executor:
    future_to_url = {executor.submit(get_code,url): url for url in links}
    for future in concurrent.futures.as_completed(future_to_url):
        try:
            url = future_to_url[future]
            code = future.result()
        except Exception as exc:
            print(f'{url} generated an exception: {exc}')
        else:
            print(f'ok! {url}')
