"""Generated from Smithy shape ``com.amazonaws.mq#__listOfUserSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mq.types.user_summary

__listOfUserSummary: TypeAlias = list["aws_sdk_mq.types.user_summary.UserSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfUserSummary) -> list:
    import aws_sdk_mq.types.user_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_mq.types.user_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfUserSummary:
    import aws_sdk_mq.types.user_summary

    out: __listOfUserSummary = []
    for item in data:
        out.append(aws_sdk_mq.types.user_summary.deserialize_json(item))
    return out
