"""Generated from Smithy shape ``com.amazonaws.cloudtrail#QueryResultRow``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.query_result_column

QueryResultRow: TypeAlias = list[
    "aws_sdk_cloudtrail.types.query_result_column.QueryResultColumn"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryResultRow) -> list:
    import aws_sdk_cloudtrail.types.query_result_column

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudtrail.types.query_result_column.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> QueryResultRow:
    import aws_sdk_cloudtrail.types.query_result_column

    out: QueryResultRow = []
    for item in data:
        out.append(
            aws_sdk_cloudtrail.types.query_result_column.deserialize_aws_json_1_1(item)
        )
    return out
