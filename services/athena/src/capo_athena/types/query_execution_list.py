"""Generated from Smithy shape ``com.amazonaws.athena#QueryExecutionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_athena.types.query_execution

QueryExecutionList: TypeAlias = list["capo_athena.types.query_execution.QueryExecution"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryExecutionList) -> list:
    import capo_athena.types.query_execution

    out: list = []
    for item in value:
        out.append(capo_athena.types.query_execution.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> QueryExecutionList:
    import capo_athena.types.query_execution

    out: QueryExecutionList = []
    for item in data:
        out.append(capo_athena.types.query_execution.deserialize_aws_json_1_1(item))
    return out
