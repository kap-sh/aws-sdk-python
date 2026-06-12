"""Generated from Smithy shape ``com.amazonaws.athena#GetQueryExecutionOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_athena.types.query_execution


class GetQueryExecutionOutput(TypedDict):
    query_execution: NotRequired["aws_sdk_athena.types.query_execution.QueryExecution"]
    """<p>Information about the query execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetQueryExecutionOutput) -> dict:
    out: dict = {}
    if "query_execution" in value:
        import aws_sdk_athena.types.query_execution

        out["QueryExecution"] = (
            aws_sdk_athena.types.query_execution.serialize_aws_json_1_1(
                value["query_execution"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetQueryExecutionOutput:
    out: GetQueryExecutionOutput = {}  # type: ignore[typeddict-item]
    if "QueryExecution" in data:
        import aws_sdk_athena.types.query_execution

        out["query_execution"] = (
            aws_sdk_athena.types.query_execution.deserialize_aws_json_1_1(
                data["QueryExecution"]
            )
        )
    return out
