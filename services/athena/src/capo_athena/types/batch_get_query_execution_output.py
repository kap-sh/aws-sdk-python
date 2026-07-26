"""Generated from Smithy shape ``com.amazonaws.athena#BatchGetQueryExecutionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.query_execution_list
    import capo_athena.types.unprocessed_query_execution_id_list


class BatchGetQueryExecutionOutput(TypedDict, closed=True):
    query_executions: NotRequired[
        "capo_athena.types.query_execution_list.QueryExecutionList"
    ]
    """<p>Information about a query execution.</p>"""
    unprocessed_query_execution_ids: NotRequired[
        "capo_athena.types.unprocessed_query_execution_id_list.UnprocessedQueryExecutionIdList"
    ]
    """<p>Information about the query executions that failed to run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetQueryExecutionOutput) -> dict:
    out: dict = {}
    if "query_executions" in value:
        import capo_athena.types.query_execution_list

        out["QueryExecutions"] = (
            capo_athena.types.query_execution_list.serialize_aws_json_1_1(
                value["query_executions"]
            )
        )
    if "unprocessed_query_execution_ids" in value:
        import capo_athena.types.unprocessed_query_execution_id_list

        out["UnprocessedQueryExecutionIds"] = (
            capo_athena.types.unprocessed_query_execution_id_list.serialize_aws_json_1_1(
                value["unprocessed_query_execution_ids"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetQueryExecutionOutput:
    out: BatchGetQueryExecutionOutput = {}  # type: ignore[typeddict-item]
    if "QueryExecutions" in data:
        import capo_athena.types.query_execution_list

        out["query_executions"] = (
            capo_athena.types.query_execution_list.deserialize_aws_json_1_1(
                data["QueryExecutions"]
            )
        )
    if "UnprocessedQueryExecutionIds" in data:
        import capo_athena.types.unprocessed_query_execution_id_list

        out["unprocessed_query_execution_ids"] = (
            capo_athena.types.unprocessed_query_execution_id_list.deserialize_aws_json_1_1(
                data["UnprocessedQueryExecutionIds"]
            )
        )
    return out
