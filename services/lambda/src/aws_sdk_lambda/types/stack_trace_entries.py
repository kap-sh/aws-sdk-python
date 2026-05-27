"""Generated from Smithy shape ``com.amazonaws.lambda#StackTraceEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lambda.types.stack_trace_entry

StackTraceEntries: TypeAlias = list[
    "aws_sdk_lambda.types.stack_trace_entry.StackTraceEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: StackTraceEntries) -> list:
    return list(value)


def deserialize_json(data: list) -> StackTraceEntries:
    return list(data)
