"""Generated from Smithy shape ``com.amazonaws.cloudtrail#QueryResultRows``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudtrail.types.query_result_row

QueryResultRows: TypeAlias = list[
    "capo_cloudtrail.types.query_result_row.QueryResultRow"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryResultRows) -> list:
    import capo_cloudtrail.types.query_result_row

    out: list = []
    for item in value:
        out.append(capo_cloudtrail.types.query_result_row.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> QueryResultRows:
    import capo_cloudtrail.types.query_result_row

    out: QueryResultRows = []
    for item in data:
        out.append(
            capo_cloudtrail.types.query_result_row.deserialize_aws_json_1_1(item)
        )
    return out
