"""Generated from Smithy shape ``com.amazonaws.pi#DimensionMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pi.types.request_string

DimensionMap: TypeAlias = dict[
    "capo_pi.types.request_string.RequestString",
    "capo_pi.types.request_string.RequestString",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: DimensionMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> DimensionMap:
    out: DimensionMap = {}
    for key, value in data.items():
        out[key] = value
    return out
