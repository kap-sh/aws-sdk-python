"""Generated from Smithy shape ``com.amazonaws.athena#UnprocessedQueryExecutionIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_athena.types.unprocessed_query_execution_id

UnprocessedQueryExecutionIdList: TypeAlias = list[
    "capo_athena.types.unprocessed_query_execution_id.UnprocessedQueryExecutionId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnprocessedQueryExecutionIdList) -> list:
    import capo_athena.types.unprocessed_query_execution_id

    out: list = []
    for item in value:
        out.append(
            capo_athena.types.unprocessed_query_execution_id.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> UnprocessedQueryExecutionIdList:
    import capo_athena.types.unprocessed_query_execution_id

    out: UnprocessedQueryExecutionIdList = []
    for item in data:
        out.append(
            capo_athena.types.unprocessed_query_execution_id.deserialize_aws_json_1_1(
                item
            )
        )
    return out
