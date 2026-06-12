"""Generated from Smithy shape ``com.amazonaws.glue#RuleMetricsMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.nullable_double

RuleMetricsMap: TypeAlias = dict[
    "aws_sdk_glue.types.name_string.NameString",
    "aws_sdk_glue.types.nullable_double.NullableDouble",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: RuleMetricsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> RuleMetricsMap:
    out: RuleMetricsMap = {}
    for key, value in data.items():
        out[key] = value
    return out
