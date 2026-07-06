"""Generated from Smithy shape ``com.amazonaws.novaact#ClientInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_nova_act.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_nova_act.types.non_blank_string


class ClientInfo(TypedDict, closed=True):
    compatibility_version: "int"
    """<p>The compatibility version of the client, used to ensure API compatibility.</p>"""
    sdk_version: NotRequired["aws_sdk_nova_act.types.non_blank_string.NonBlankString"]
    """<p>The version of the SDK being used by the client.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClientInfo) -> dict:
    out: dict = {}
    out["compatibilityVersion"] = value["compatibility_version"]
    if "sdk_version" in value:
        out["sdkVersion"] = value["sdk_version"]
    return out


def deserialize_json(data: dict) -> ClientInfo:
    out: ClientInfo = {}  # type: ignore[typeddict-item]
    if "compatibilityVersion" in data:
        out["compatibility_version"] = data["compatibilityVersion"]
    else:
        raise DeserializationError("ClientInfo.compatibility_version required")
    if "sdkVersion" in data:
        out["sdk_version"] = data["sdkVersion"]
    return out
