"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomationruntime#OutputSegment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation_runtime.types.custom_output_status


class OutputSegment(TypedDict, closed=True):
    custom_output_status: NotRequired[
        "capo_bedrock_data_automation_runtime.types.custom_output_status.CustomOutputStatus"
    ]
    """Status of blueprint match"""
    custom_output: NotRequired["str"]
    """Custom output response"""
    standard_output: NotRequired["str"]
    """Standard output response"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OutputSegment) -> dict:
    out: dict = {}
    if "custom_output_status" in value:
        import capo_bedrock_data_automation_runtime.types.custom_output_status

        out["customOutputStatus"] = (
            capo_bedrock_data_automation_runtime.types.custom_output_status.serialize_aws_json_1_1(
                value["custom_output_status"]
            )
        )
    if "custom_output" in value:
        out["customOutput"] = value["custom_output"]
    if "standard_output" in value:
        out["standardOutput"] = value["standard_output"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OutputSegment:
    out: OutputSegment = {}  # type: ignore[typeddict-item]
    if "customOutputStatus" in data:
        import capo_bedrock_data_automation_runtime.types.custom_output_status

        out["custom_output_status"] = (
            capo_bedrock_data_automation_runtime.types.custom_output_status.deserialize_aws_json_1_1(
                data["customOutputStatus"]
            )
        )
    if "customOutput" in data:
        out["custom_output"] = data["customOutput"]
    if "standardOutput" in data:
        out["standard_output"] = data["standardOutput"]
    return out
