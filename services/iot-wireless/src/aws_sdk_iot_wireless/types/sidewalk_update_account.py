"""Generated from Smithy shape ``com.amazonaws.iotwireless#SidewalkUpdateAccount``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.app_server_private_key


class SidewalkUpdateAccount(TypedDict):
    app_server_private_key: NotRequired[
        "aws_sdk_iot_wireless.types.app_server_private_key.AppServerPrivateKey"
    ]
    """<p>The new Sidewalk application server private key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SidewalkUpdateAccount) -> dict:
    out: dict = {}
    if "app_server_private_key" in value:
        out["AppServerPrivateKey"] = value["app_server_private_key"]
    return out


def deserialize_json(data: dict) -> SidewalkUpdateAccount:
    out: SidewalkUpdateAccount = {}  # type: ignore[typeddict-item]
    if "AppServerPrivateKey" in data:
        out["app_server_private_key"] = data["AppServerPrivateKey"]
    return out
