"""Generated from Smithy shape ``com.amazonaws.lambda#ListDurableExecutionsByFunctionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.durable_executions
    import capo_lambda.types.string


class ListDurableExecutionsByFunctionResponse(TypedDict, closed=True):
    durable_executions: NotRequired[
        "capo_lambda.types.durable_executions.DurableExecutions"
    ]
    """<p>List of durable execution summaries matching the filter criteria.</p>"""
    next_marker: NotRequired["capo_lambda.types.string.String"]
    """<p>Pagination token for retrieving additional results. Present only if there are more results available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDurableExecutionsByFunctionResponse) -> dict:
    out: dict = {}
    if "durable_executions" in value:
        import capo_lambda.types.durable_executions

        out["DurableExecutions"] = capo_lambda.types.durable_executions.serialize_json(
            value["durable_executions"]
        )
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    return out


def deserialize_json(data: dict) -> ListDurableExecutionsByFunctionResponse:
    out: ListDurableExecutionsByFunctionResponse = {}  # type: ignore[typeddict-item]
    if "DurableExecutions" in data:
        import capo_lambda.types.durable_executions

        out["durable_executions"] = (
            capo_lambda.types.durable_executions.deserialize_json(
                data["DurableExecutions"]
            )
        )
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    return out
