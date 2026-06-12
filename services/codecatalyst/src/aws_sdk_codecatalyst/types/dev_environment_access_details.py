"""Generated from Smithy shape ``com.amazonaws.codecatalyst#DevEnvironmentAccessDetails``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codecatalyst.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecatalyst.types.sensitive_string


class DevEnvironmentAccessDetails(TypedDict):
    stream_url: "aws_sdk_codecatalyst.types.sensitive_string.SensitiveString"
    """<p>The URL used to send commands to and from the Dev Environment.</p>"""
    token_value: "aws_sdk_codecatalyst.types.sensitive_string.SensitiveString"
    """<p>An encrypted token value that contains session and caller information used to authenticate the connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DevEnvironmentAccessDetails) -> dict:
    out: dict = {}
    out["streamUrl"] = value["stream_url"]
    out["tokenValue"] = value["token_value"]
    return out


def deserialize_json(data: dict) -> DevEnvironmentAccessDetails:
    out: DevEnvironmentAccessDetails = {}  # type: ignore[typeddict-item]
    if "streamUrl" in data:
        out["stream_url"] = data["streamUrl"]
    else:
        raise DeserializationError("DevEnvironmentAccessDetails.stream_url required")
    if "tokenValue" in data:
        out["token_value"] = data["tokenValue"]
    else:
        raise DeserializationError("DevEnvironmentAccessDetails.token_value required")
    return out
