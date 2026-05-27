"""Generated from Smithy shape ``com.amazonaws.lambda#Concurrency``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.reserved_concurrent_executions


class Concurrency(TypedDict):
    reserved_concurrent_executions: NotRequired[
        "aws_sdk_lambda.types.reserved_concurrent_executions.ReservedConcurrentExecutions"
    ]
    """<p>The number of concurrent executions that are reserved for this function. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html\">Managing Lambda reserved concurrency</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Concurrency) -> dict:
    out: dict = {}
    if "reserved_concurrent_executions" in value:
        out["ReservedConcurrentExecutions"] = value["reserved_concurrent_executions"]
    return out


def deserialize_json(data: dict) -> Concurrency:
    out: Concurrency = {}  # type: ignore[typeddict-item]
    if "ReservedConcurrentExecutions" in data:
        out["reserved_concurrent_executions"] = data["ReservedConcurrentExecutions"]
    return out
