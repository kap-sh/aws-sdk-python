"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#ChannelRetentionSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_identity.types.retention_days


class ChannelRetentionSettings(TypedDict):
    retention_days: NotRequired[
        "aws_sdk_chime_sdk_identity.types.retention_days.RetentionDays"
    ]
    """<p>The time in days to retain the messages in a channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChannelRetentionSettings) -> dict:
    out: dict = {}
    if "retention_days" in value:
        out["RetentionDays"] = value["retention_days"]
    return out


def deserialize_json(data: dict) -> ChannelRetentionSettings:
    out: ChannelRetentionSettings = {}  # type: ignore[typeddict-item]
    if "RetentionDays" in data:
        out["retention_days"] = data["RetentionDays"]
    return out
