"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomationruntime#InvokeDataAutomationAsyncResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_data_automation_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation_runtime.types.invocation_arn


class InvokeDataAutomationAsyncResponse(TypedDict):
    invocation_arn: (
        "aws_sdk_bedrock_data_automation_runtime.types.invocation_arn.InvocationArn"
    )
    """ARN of the automation job"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvokeDataAutomationAsyncResponse) -> dict:
    out: dict = {}
    out["invocationArn"] = value["invocation_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvokeDataAutomationAsyncResponse:
    out: InvokeDataAutomationAsyncResponse = {}  # type: ignore[typeddict-item]
    if "invocationArn" in data:
        out["invocation_arn"] = data["invocationArn"]
    else:
        raise DeserializationError(
            "InvokeDataAutomationAsyncResponse.invocation_arn required"
        )
    return out
