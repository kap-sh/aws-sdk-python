"""Generated from Smithy shape ``com.amazonaws.qconnect#FailureReason``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.non_empty_string

FailureReason: TypeAlias = list[
    "aws_sdk_qconnect.types.non_empty_string.NonEmptyString"
]


# --- restJson1 ser/de ---
def serialize_json(value: FailureReason) -> list:
    return list(value)


def deserialize_json(data: list) -> FailureReason:
    return list(data)
