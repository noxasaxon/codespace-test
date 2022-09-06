from result import as_result
import requests


def test_as_result_3rd_party_fn() -> None:
    """
    The ``as_result()`` is a signature-preserving decorator.
    """

    request_nt = as_result(BaseException)(requests.request)

    test = request_nt(method="GET", url="http://google.com")
    print(test.unwrap())


test_as_result_3rd_party_fn()
