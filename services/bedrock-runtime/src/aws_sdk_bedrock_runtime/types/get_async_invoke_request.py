"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GetAsyncInvokeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.invocation_arn


class GetAsyncInvokeRequest(TypedDict, closed=True):
    invocation_arn: "aws_sdk_bedrock_runtime.types.invocation_arn.InvocationArn"
    """<p>The invocation's ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAsyncInvokeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAsyncInvokeRequest:
    out: GetAsyncInvokeRequest = {}  # type: ignore[typeddict-item]
    return out
