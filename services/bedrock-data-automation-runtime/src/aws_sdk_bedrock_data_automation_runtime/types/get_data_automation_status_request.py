"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomationruntime#GetDataAutomationStatusRequest``."""

from typing import TYPE_CHECKING, TypedDict
if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation_runtime.types.invocation_arn

class GetDataAutomationStatusRequest(TypedDict):
    invocation_arn: "aws_sdk_bedrock_data_automation_runtime.types.invocation_arn.InvocationArn"
    """Invocation arn."""

# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDataAutomationStatusRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDataAutomationStatusRequest:
    out: GetDataAutomationStatusRequest = {}  # type: ignore[typeddict-item]
    return out