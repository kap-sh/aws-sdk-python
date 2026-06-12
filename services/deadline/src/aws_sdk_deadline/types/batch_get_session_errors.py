"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetSessionErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.batch_get_session_error

BatchGetSessionErrors: TypeAlias = list[
    "aws_sdk_deadline.types.batch_get_session_error.BatchGetSessionError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetSessionErrors) -> list:
    import aws_sdk_deadline.types.batch_get_session_error

    out: list = []
    for item in value:
        out.append(aws_sdk_deadline.types.batch_get_session_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchGetSessionErrors:
    import aws_sdk_deadline.types.batch_get_session_error

    out: BatchGetSessionErrors = []
    for item in data:
        out.append(
            aws_sdk_deadline.types.batch_get_session_error.deserialize_json(item)
        )
    return out
