"""Generated from Smithy shape ``com.amazonaws.medialive#OutputDestinationSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class OutputDestinationSettings(TypedDict, closed=True):
    password_param: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """key used to extract the password from EC2 Parameter store"""
    stream_name: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Stream name for RTMP destinations (URLs of type rtmp://)"""
    url: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """A URL specifying a destination"""
    username: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """username for destination"""


# --- restJson1 ser/de ---
def serialize_json(value: OutputDestinationSettings) -> dict:
    out: dict = {}
    if "password_param" in value:
        out["passwordParam"] = value["password_param"]
    if "stream_name" in value:
        out["streamName"] = value["stream_name"]
    if "url" in value:
        out["url"] = value["url"]
    if "username" in value:
        out["username"] = value["username"]
    return out


def deserialize_json(data: dict) -> OutputDestinationSettings:
    out: OutputDestinationSettings = {}  # type: ignore[typeddict-item]
    if "passwordParam" in data:
        out["password_param"] = data["passwordParam"]
    if "streamName" in data:
        out["stream_name"] = data["streamName"]
    if "url" in data:
        out["url"] = data["url"]
    if "username" in data:
        out["username"] = data["username"]
    return out
