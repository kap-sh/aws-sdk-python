"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetSessionItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.batch_get_session_item

BatchGetSessionItems: TypeAlias = list[
    "aws_sdk_deadline.types.batch_get_session_item.BatchGetSessionItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetSessionItems) -> list:
    import aws_sdk_deadline.types.batch_get_session_item

    out: list = []
    for item in value:
        out.append(aws_sdk_deadline.types.batch_get_session_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchGetSessionItems:
    import aws_sdk_deadline.types.batch_get_session_item

    out: BatchGetSessionItems = []
    for item in data:
        out.append(aws_sdk_deadline.types.batch_get_session_item.deserialize_json(item))
    return out
