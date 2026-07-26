"""Generated from Smithy shape ``com.amazonaws.glue#PropertyNameOverrides``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.property_name

PropertyNameOverrides: TypeAlias = dict[
    "capo_glue.types.property_name.PropertyName",
    "capo_glue.types.property_name.PropertyName",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: PropertyNameOverrides) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> PropertyNameOverrides:
    out: PropertyNameOverrides = {}
    for key, value in data.items():
        out[key] = value
    return out
