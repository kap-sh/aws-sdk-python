"""Generated from Smithy shape ``com.amazonaws.medialive#DescribePrimaryChannelSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of__string
    import aws_sdk_medialive.types.linked_channel_type


class DescribePrimaryChannelSettings(TypedDict, closed=True):
    following_channel_arns: NotRequired[
        "aws_sdk_medialive.types.__list_of__string.__listOf__string"
    ]
    """The ARNs of the following channels for this primary channel"""
    linked_channel_type: NotRequired[
        "aws_sdk_medialive.types.linked_channel_type.LinkedChannelType"
    ]
    """Specifies this as a primary channel"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribePrimaryChannelSettings) -> dict:
    out: dict = {}
    if "following_channel_arns" in value:
        import aws_sdk_medialive.types.__list_of__string

        out["followingChannelArns"] = (
            aws_sdk_medialive.types.__list_of__string.serialize_json(
                value["following_channel_arns"]
            )
        )
    if "linked_channel_type" in value:
        import aws_sdk_medialive.types.linked_channel_type

        out["linkedChannelType"] = (
            aws_sdk_medialive.types.linked_channel_type.serialize_json(
                value["linked_channel_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribePrimaryChannelSettings:
    out: DescribePrimaryChannelSettings = {}  # type: ignore[typeddict-item]
    if "followingChannelArns" in data:
        import aws_sdk_medialive.types.__list_of__string

        out["following_channel_arns"] = (
            aws_sdk_medialive.types.__list_of__string.deserialize_json(
                data["followingChannelArns"]
            )
        )
    if "linkedChannelType" in data:
        import aws_sdk_medialive.types.linked_channel_type

        out["linked_channel_type"] = (
            aws_sdk_medialive.types.linked_channel_type.deserialize_json(
                data["linkedChannelType"]
            )
        )
    return out
