"""Generated from Smithy shape ``com.amazonaws.glue#EvaluatedMetricsMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.name_string
    import capo_glue.types.nullable_double

EvaluatedMetricsMap: TypeAlias = dict[
    "capo_glue.types.name_string.NameString",
    "capo_glue.types.nullable_double.NullableDouble",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: EvaluatedMetricsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> EvaluatedMetricsMap:
    out: EvaluatedMetricsMap = {}
    for key, value in data.items():
        out[key] = value
    return out
