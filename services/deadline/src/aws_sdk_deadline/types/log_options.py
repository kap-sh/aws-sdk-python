"""Generated from Smithy shape ``com.amazonaws.deadline#LogOptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.string

LogOptions: TypeAlias = dict[
    "aws_sdk_deadline.types.string.String", "aws_sdk_deadline.types.string.String"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: LogOptions) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> LogOptions:
    out: LogOptions = {}
    for key, value in data.items():
        out[key] = value
    return out
