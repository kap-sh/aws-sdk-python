"""Generated from Smithy shape ``com.amazonaws.cloudtrail#QueryParameterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudtrail.types.query_parameter_key
    import capo_cloudtrail.types.query_parameter_value

QueryParameterValues: TypeAlias = dict[
    "capo_cloudtrail.types.query_parameter_key.QueryParameterKey",
    "capo_cloudtrail.types.query_parameter_value.QueryParameterValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: QueryParameterValues) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> QueryParameterValues:
    out: QueryParameterValues = {}
    for key, value in data.items():
        out[key] = value
    return out
