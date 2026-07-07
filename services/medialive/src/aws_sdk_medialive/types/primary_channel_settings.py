"""Generated from Smithy shape ``com.amazonaws.medialive#PrimaryChannelSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.linked_channel_type


class PrimaryChannelSettings(TypedDict, closed=True):
    linked_channel_type: NotRequired[
        "aws_sdk_medialive.types.linked_channel_type.LinkedChannelType"
    ]
    """Specifies this as a primary channel"""


# --- restJson1 ser/de ---
def serialize_json(value: PrimaryChannelSettings) -> dict:
    out: dict = {}
    if "linked_channel_type" in value:
        import aws_sdk_medialive.types.linked_channel_type

        out["linkedChannelType"] = (
            aws_sdk_medialive.types.linked_channel_type.serialize_json(
                value["linked_channel_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> PrimaryChannelSettings:
    out: PrimaryChannelSettings = {}  # type: ignore[typeddict-item]
    if "linkedChannelType" in data:
        import aws_sdk_medialive.types.linked_channel_type

        out["linked_channel_type"] = (
            aws_sdk_medialive.types.linked_channel_type.deserialize_json(
                data["linkedChannelType"]
            )
        )
    return out
