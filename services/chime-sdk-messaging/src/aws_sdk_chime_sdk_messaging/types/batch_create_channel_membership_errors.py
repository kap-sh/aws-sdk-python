"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#BatchCreateChannelMembershipErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.batch_create_channel_membership_error

BatchCreateChannelMembershipErrors: TypeAlias = list[
    "aws_sdk_chime_sdk_messaging.types.batch_create_channel_membership_error.BatchCreateChannelMembershipError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateChannelMembershipErrors) -> list:
    import aws_sdk_chime_sdk_messaging.types.batch_create_channel_membership_error

    out: list = []
    for item in value:
        out.append(
            aws_sdk_chime_sdk_messaging.types.batch_create_channel_membership_error.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchCreateChannelMembershipErrors:
    import aws_sdk_chime_sdk_messaging.types.batch_create_channel_membership_error

    out: BatchCreateChannelMembershipErrors = []
    for item in data:
        out.append(
            aws_sdk_chime_sdk_messaging.types.batch_create_channel_membership_error.deserialize_json(
                item
            )
        )
    return out
