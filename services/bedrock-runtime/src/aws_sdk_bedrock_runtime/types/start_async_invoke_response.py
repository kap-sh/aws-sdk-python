"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#StartAsyncInvokeResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.invocation_arn


class StartAsyncInvokeResponse(TypedDict):
    invocation_arn: "aws_sdk_bedrock_runtime.types.invocation_arn.InvocationArn"
    """<p>The ARN of the invocation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartAsyncInvokeResponse) -> dict:
    out: dict = {}
    out["invocationArn"] = value["invocation_arn"]
    return out


def deserialize_json(data: dict) -> StartAsyncInvokeResponse:
    out: StartAsyncInvokeResponse = {}  # type: ignore[typeddict-item]
    if "invocationArn" in data:
        out["invocation_arn"] = data["invocationArn"]
    else:
        raise DeserializationError("StartAsyncInvokeResponse.invocation_arn required")
    return out
