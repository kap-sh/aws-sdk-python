"""Generated from Smithy shape ``com.amazonaws.lambda#GetFunctionConcurrencyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.reserved_concurrent_executions


class GetFunctionConcurrencyResponse(TypedDict, closed=True):
    reserved_concurrent_executions: NotRequired[
        "capo_lambda.types.reserved_concurrent_executions.ReservedConcurrentExecutions"
    ]
    """<p>The number of simultaneous executions that are reserved for the function.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFunctionConcurrencyResponse) -> dict:
    out: dict = {}
    if "reserved_concurrent_executions" in value:
        out["ReservedConcurrentExecutions"] = value["reserved_concurrent_executions"]
    return out


def deserialize_json(data: dict) -> GetFunctionConcurrencyResponse:
    out: GetFunctionConcurrencyResponse = {}  # type: ignore[typeddict-item]
    if "ReservedConcurrentExecutions" in data:
        out["reserved_concurrent_executions"] = data["ReservedConcurrentExecutions"]
    return out
