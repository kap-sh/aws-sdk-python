"""Generated from Smithy shape ``com.amazonaws.lambda#GetDurableExecutionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lambda.types.durable_execution_arn


class GetDurableExecutionRequest(TypedDict):
    durable_execution_arn: (
        "aws_sdk_lambda.types.durable_execution_arn.DurableExecutionArn"
    )
    """<p>The Amazon Resource Name (ARN) of the durable execution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDurableExecutionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDurableExecutionRequest:
    out: GetDurableExecutionRequest = {}  # type: ignore[typeddict-item]
    return out
