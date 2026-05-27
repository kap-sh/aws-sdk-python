"""Generated from Smithy shape ``com.amazonaws.lambda#GetFunctionConcurrencyResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.reserved_concurrent_executions


class GetFunctionConcurrencyResponse(TypedDict):
    reserved_concurrent_executions: NotRequired[
        "aws_sdk_lambda.types.reserved_concurrent_executions.ReservedConcurrentExecutions"
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
