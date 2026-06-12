"""Generated from Smithy shape ``com.amazonaws.ssm#AutomationExecutionMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.automation_execution_metadata

AutomationExecutionMetadataList: TypeAlias = list[
    "aws_sdk_ssm.types.automation_execution_metadata.AutomationExecutionMetadata"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutomationExecutionMetadataList) -> list:
    import aws_sdk_ssm.types.automation_execution_metadata

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ssm.types.automation_execution_metadata.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AutomationExecutionMetadataList:
    import aws_sdk_ssm.types.automation_execution_metadata

    out: AutomationExecutionMetadataList = []
    for item in data:
        out.append(
            aws_sdk_ssm.types.automation_execution_metadata.deserialize_aws_json_1_1(
                item
            )
        )
    return out
