"""Generated from Smithy shape ``com.amazonaws.athena#QueryExecutionIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_athena.types.query_execution_id

QueryExecutionIdList: TypeAlias = list[
    "capo_athena.types.query_execution_id.QueryExecutionId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryExecutionIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> QueryExecutionIdList:
    return list(data)
