"""Generated from Smithy shape ``com.amazonaws.cloudtrail#QueryResultColumn``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.query_result_key
    import aws_sdk_cloudtrail.types.query_result_value

QueryResultColumn: TypeAlias = dict[
    "aws_sdk_cloudtrail.types.query_result_key.QueryResultKey",
    "aws_sdk_cloudtrail.types.query_result_value.QueryResultValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: QueryResultColumn) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> QueryResultColumn:
    out: QueryResultColumn = {}
    for key, value in data.items():
        out[key] = value
    return out
