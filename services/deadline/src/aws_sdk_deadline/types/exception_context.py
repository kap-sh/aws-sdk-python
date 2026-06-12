"""Generated from Smithy shape ``com.amazonaws.deadline#ExceptionContext``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.string

ExceptionContext: TypeAlias = dict[
    "aws_sdk_deadline.types.string.String", "aws_sdk_deadline.types.string.String"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ExceptionContext) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ExceptionContext:
    out: ExceptionContext = {}
    for key, value in data.items():
        out[key] = value
    return out
