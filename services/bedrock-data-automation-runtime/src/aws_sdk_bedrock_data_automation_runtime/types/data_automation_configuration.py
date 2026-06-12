"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomationruntime#DataAutomationConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock_data_automation_runtime.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation_runtime.types.data_automation_arn
    import aws_sdk_bedrock_data_automation_runtime.types.data_automation_stage

class DataAutomationConfiguration(TypedDict):
    data_automation_project_arn: "aws_sdk_bedrock_data_automation_runtime.types.data_automation_arn.DataAutomationArn"
    """Data automation project arn."""
    stage: NotRequired["aws_sdk_bedrock_data_automation_runtime.types.data_automation_stage.DataAutomationStage"]
    """Data automation stage."""

# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataAutomationConfiguration) -> dict:
    out: dict = {}
    out["dataAutomationProjectArn"] = value["data_automation_project_arn"]
    if "stage" in value:
        import aws_sdk_bedrock_data_automation_runtime.types.data_automation_stage
        out["stage"] = aws_sdk_bedrock_data_automation_runtime.types.data_automation_stage.serialize_aws_json_1_1(value["stage"])
    return out


def deserialize_aws_json_1_1(data: dict) -> DataAutomationConfiguration:
    out: DataAutomationConfiguration = {}  # type: ignore[typeddict-item]
    if "dataAutomationProjectArn" in data:
        out["data_automation_project_arn"] = data["dataAutomationProjectArn"]
    else:
        raise DeserializationError("DataAutomationConfiguration.data_automation_project_arn required")
    if "stage" in data:
        import aws_sdk_bedrock_data_automation_runtime.types.data_automation_stage
        out["stage"] = aws_sdk_bedrock_data_automation_runtime.types.data_automation_stage.deserialize_aws_json_1_1(data["stage"])
    return out