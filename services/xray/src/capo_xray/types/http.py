"""Generated from Smithy shape ``com.amazonaws.xray#Http``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.nullable_integer
    import capo_xray.types.string


class Http(TypedDict, closed=True):
    http_url: NotRequired["capo_xray.types.string.String"]
    """<p>The request URL.</p>"""
    http_status: NotRequired["capo_xray.types.nullable_integer.NullableInteger"]
    """<p>The response status.</p>"""
    http_method: NotRequired["capo_xray.types.string.String"]
    """<p>The request method.</p>"""
    user_agent: NotRequired["capo_xray.types.string.String"]
    """<p>The request's user agent string.</p>"""
    client_ip: NotRequired["capo_xray.types.string.String"]
    """<p>The IP address of the requestor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Http) -> dict:
    out: dict = {}
    if "http_url" in value:
        out["HttpURL"] = value["http_url"]
    if "http_status" in value:
        out["HttpStatus"] = value["http_status"]
    if "http_method" in value:
        out["HttpMethod"] = value["http_method"]
    if "user_agent" in value:
        out["UserAgent"] = value["user_agent"]
    if "client_ip" in value:
        out["ClientIp"] = value["client_ip"]
    return out


def deserialize_json(data: dict) -> Http:
    out: Http = {}  # type: ignore[typeddict-item]
    if "HttpURL" in data:
        out["http_url"] = data["HttpURL"]
    if "HttpStatus" in data:
        out["http_status"] = data["HttpStatus"]
    if "HttpMethod" in data:
        out["http_method"] = data["HttpMethod"]
    if "UserAgent" in data:
        out["user_agent"] = data["UserAgent"]
    if "ClientIp" in data:
        out["client_ip"] = data["ClientIp"]
    return out
