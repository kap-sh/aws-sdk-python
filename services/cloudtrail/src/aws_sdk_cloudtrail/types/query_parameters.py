"""Generated from Smithy shape ``com.amazonaws.cloudtrail#QueryParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.query_parameter

QueryParameters: TypeAlias = list[
    "aws_sdk_cloudtrail.types.query_parameter.QueryParameter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryParameters) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> QueryParameters:
    return list(data)
