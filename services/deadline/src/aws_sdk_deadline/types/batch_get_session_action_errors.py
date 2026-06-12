"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetSessionActionErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.batch_get_session_action_error

BatchGetSessionActionErrors: TypeAlias = list[
    "aws_sdk_deadline.types.batch_get_session_action_error.BatchGetSessionActionError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetSessionActionErrors) -> list:
    import aws_sdk_deadline.types.batch_get_session_action_error

    out: list = []
    for item in value:
        out.append(
            aws_sdk_deadline.types.batch_get_session_action_error.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BatchGetSessionActionErrors:
    import aws_sdk_deadline.types.batch_get_session_action_error

    out: BatchGetSessionActionErrors = []
    for item in data:
        out.append(
            aws_sdk_deadline.types.batch_get_session_action_error.deserialize_json(item)
        )
    return out
