"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomationruntime#GetDataAutomationStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_data_automation_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_data_automation_runtime.types.invocation_arn


class GetDataAutomationStatusRequest(TypedDict, closed=True):
    invocation_arn: (
        "capo_bedrock_data_automation_runtime.types.invocation_arn.InvocationArn"
    )
    """Invocation arn."""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDataAutomationStatusRequest) -> dict:
    out: dict = {}
    out["invocationArn"] = value["invocation_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDataAutomationStatusRequest:
    out: GetDataAutomationStatusRequest = {}  # type: ignore[typeddict-item]
    if data.get("invocationArn") is not None:
        out["invocation_arn"] = data["invocationArn"]
    else:
        raise DeserializationError(
            "GetDataAutomationStatusRequest.invocation_arn required"
        )
    return out
