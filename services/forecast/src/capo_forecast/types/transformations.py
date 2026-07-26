"""Generated from Smithy shape ``com.amazonaws.forecast#Transformations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_forecast.types.name
    import capo_forecast.types.value

Transformations: TypeAlias = dict[
    "capo_forecast.types.name.Name", "capo_forecast.types.value.Value"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: Transformations) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> Transformations:
    out: Transformations = {}
    for key, value in data.items():
        out[key] = value
    return out
