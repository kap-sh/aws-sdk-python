"""Generated from Smithy shape ``com.amazonaws.cloudtrail#QueryResultRow``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudtrail.types.query_result_column

QueryResultRow: TypeAlias = list[
    "capo_cloudtrail.types.query_result_column.QueryResultColumn"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryResultRow) -> list:
    import capo_cloudtrail.types.query_result_column

    out: list = []
    for item in value:
        out.append(
            capo_cloudtrail.types.query_result_column.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> QueryResultRow:
    import capo_cloudtrail.types.query_result_column

    out: QueryResultRow = []
    for item in data:
        out.append(
            capo_cloudtrail.types.query_result_column.deserialize_aws_json_1_1(item)
        )
    return out
