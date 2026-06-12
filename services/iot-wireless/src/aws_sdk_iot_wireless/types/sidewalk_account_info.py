"""Generated from Smithy shape ``com.amazonaws.iotwireless#SidewalkAccountInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.amazon_id
    import aws_sdk_iot_wireless.types.app_server_private_key


class SidewalkAccountInfo(TypedDict):
    amazon_id: NotRequired["aws_sdk_iot_wireless.types.amazon_id.AmazonId"]
    """<p>The Sidewalk Amazon ID.</p>"""
    app_server_private_key: NotRequired[
        "aws_sdk_iot_wireless.types.app_server_private_key.AppServerPrivateKey"
    ]
    """<p>The Sidewalk application server private key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SidewalkAccountInfo) -> dict:
    out: dict = {}
    if "amazon_id" in value:
        out["AmazonId"] = value["amazon_id"]
    if "app_server_private_key" in value:
        out["AppServerPrivateKey"] = value["app_server_private_key"]
    return out


def deserialize_json(data: dict) -> SidewalkAccountInfo:
    out: SidewalkAccountInfo = {}  # type: ignore[typeddict-item]
    if "AmazonId" in data:
        out["amazon_id"] = data["AmazonId"]
    if "AppServerPrivateKey" in data:
        out["app_server_private_key"] = data["AppServerPrivateKey"]
    return out
