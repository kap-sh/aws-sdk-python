"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetSessionActionItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.batch_get_session_action_item

BatchGetSessionActionItems: TypeAlias = list[
    "aws_sdk_deadline.types.batch_get_session_action_item.BatchGetSessionActionItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetSessionActionItems) -> list:
    import aws_sdk_deadline.types.batch_get_session_action_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_deadline.types.batch_get_session_action_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BatchGetSessionActionItems:
    import aws_sdk_deadline.types.batch_get_session_action_item

    out: BatchGetSessionActionItems = []
    for item in data:
        out.append(
            aws_sdk_deadline.types.batch_get_session_action_item.deserialize_json(item)
        )
    return out
