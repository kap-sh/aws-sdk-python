"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#NotificationDestinationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_kinesis_video.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_video.types.destination_uri


class NotificationDestinationConfig(TypedDict, closed=True):
    uri: "aws_sdk_kinesis_video.types.destination_uri.DestinationUri"
    """<p>The Uniform Resource Identifier (URI) that identifies where the images will be delivered.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotificationDestinationConfig) -> dict:
    out: dict = {}
    out["Uri"] = value["uri"]
    return out


def deserialize_json(data: dict) -> NotificationDestinationConfig:
    out: NotificationDestinationConfig = {}  # type: ignore[typeddict-item]
    if "Uri" in data:
        out["uri"] = data["Uri"]
    else:
        raise DeserializationError("NotificationDestinationConfig.uri required")
    return out
