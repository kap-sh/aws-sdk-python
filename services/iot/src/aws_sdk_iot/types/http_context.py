"""Generated from Smithy shape ``com.amazonaws.iot#HttpContext``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.http_headers
    import aws_sdk_iot.types.http_query_string


class HttpContext(TypedDict, closed=True):
    headers: NotRequired["aws_sdk_iot.types.http_headers.HttpHeaders"]
    """<p>The header keys and values in an HTTP authorization request.</p>"""
    query_string: NotRequired["aws_sdk_iot.types.http_query_string.HttpQueryString"]
    """<p>The query string keys and values in an HTTP authorization request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HttpContext) -> dict:
    out: dict = {}
    if "headers" in value:
        import aws_sdk_iot.types.http_headers

        out["headers"] = aws_sdk_iot.types.http_headers.serialize_json(value["headers"])
    if "query_string" in value:
        out["queryString"] = value["query_string"]
    return out


def deserialize_json(data: dict) -> HttpContext:
    out: HttpContext = {}  # type: ignore[typeddict-item]
    if "headers" in data:
        import aws_sdk_iot.types.http_headers

        out["headers"] = aws_sdk_iot.types.http_headers.deserialize_json(
            data["headers"]
        )
    if "queryString" in data:
        out["query_string"] = data["queryString"]
    return out
