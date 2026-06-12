"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#SingleMasterConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kinesis_video.types.message_ttl_seconds


class SingleMasterConfiguration(TypedDict):
    message_ttl_seconds: NotRequired[
        "aws_sdk_kinesis_video.types.message_ttl_seconds.MessageTtlSeconds"
    ]
    """<p>The period of time (in seconds) a signaling channel retains undelivered messages before they are discarded. Use to update this value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SingleMasterConfiguration) -> dict:
    out: dict = {}
    if "message_ttl_seconds" in value:
        out["MessageTtlSeconds"] = value["message_ttl_seconds"]
    return out


def deserialize_json(data: dict) -> SingleMasterConfiguration:
    out: SingleMasterConfiguration = {}  # type: ignore[typeddict-item]
    if "MessageTtlSeconds" in data:
        out["message_ttl_seconds"] = data["MessageTtlSeconds"]
    return out
