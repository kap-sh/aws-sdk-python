"""Generated from Smithy shape ``com.amazonaws.batch#ArrayJobStatusSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_batch.types.integer
    import aws_sdk_batch.types.string

ArrayJobStatusSummary: TypeAlias = dict[
    "aws_sdk_batch.types.string.String", "aws_sdk_batch.types.integer.Integer"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ArrayJobStatusSummary) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ArrayJobStatusSummary:
    out: ArrayJobStatusSummary = {}
    for key, value in data.items():
        out[key] = value
    return out
