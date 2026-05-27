"""Generated from Smithy shape ``com.amazonaws.lambda#ListDurableExecutionsByFunctionResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.durable_executions
    import aws_sdk_lambda.types.string


class ListDurableExecutionsByFunctionResponse(TypedDict):
    durable_executions: NotRequired[
        "aws_sdk_lambda.types.durable_executions.DurableExecutions"
    ]
    """<p>List of durable execution summaries matching the filter criteria.</p>"""
    next_marker: NotRequired["aws_sdk_lambda.types.string.String"]
    """<p>Pagination token for retrieving additional results. Present only if there are more results available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDurableExecutionsByFunctionResponse) -> dict:
    out: dict = {}
    if "durable_executions" in value:
        import aws_sdk_lambda.types.durable_executions

        out["DurableExecutions"] = (
            aws_sdk_lambda.types.durable_executions.serialize_json(
                value["durable_executions"]
            )
        )
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    return out


def deserialize_json(data: dict) -> ListDurableExecutionsByFunctionResponse:
    out: ListDurableExecutionsByFunctionResponse = {}  # type: ignore[typeddict-item]
    if "DurableExecutions" in data:
        import aws_sdk_lambda.types.durable_executions

        out["durable_executions"] = (
            aws_sdk_lambda.types.durable_executions.deserialize_json(
                data["DurableExecutions"]
            )
        )
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    return out
