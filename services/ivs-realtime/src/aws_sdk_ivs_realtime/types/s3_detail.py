"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#S3Detail``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ivs_realtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.string


class S3Detail(TypedDict):
    recording_prefix: "aws_sdk_ivs_realtime.types.string.String"
    """<p>The S3 bucket prefix under which the recording is stored.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Detail) -> dict:
    out: dict = {}
    out["recordingPrefix"] = value["recording_prefix"]
    return out


def deserialize_json(data: dict) -> S3Detail:
    out: S3Detail = {}  # type: ignore[typeddict-item]
    if "recordingPrefix" in data:
        out["recording_prefix"] = data["recordingPrefix"]
    else:
        raise DeserializationError("S3Detail.recording_prefix required")
    return out
