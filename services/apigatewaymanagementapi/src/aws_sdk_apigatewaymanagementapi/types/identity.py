"""Generated from Smithy shape ``com.amazonaws.apigatewaymanagementapi#Identity``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apigatewaymanagementapi.types.__string


class Identity(TypedDict):
    source_ip: NotRequired["aws_sdk_apigatewaymanagementapi.types.__string.__string"]
    """<p>The source IP address of the TCP connection making the request to API Gateway.</p>"""
    user_agent: NotRequired["aws_sdk_apigatewaymanagementapi.types.__string.__string"]
    """<p>The User Agent of the API caller.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Identity) -> dict:
    out: dict = {}
    if "source_ip" in value:
        out["sourceIp"] = value["source_ip"]
    if "user_agent" in value:
        out["userAgent"] = value["user_agent"]
    return out


def deserialize_json(data: dict) -> Identity:
    out: Identity = {}  # type: ignore[typeddict-item]
    if "sourceIp" in data:
        out["source_ip"] = data["sourceIp"]
    if "userAgent" in data:
        out["user_agent"] = data["userAgent"]
    return out
