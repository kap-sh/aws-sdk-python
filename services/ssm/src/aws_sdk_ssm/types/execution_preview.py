"""Generated from Smithy shape ``com.amazonaws.ssm#ExecutionPreview``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_ssm.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.automation_execution_preview


class _ExecutionPreview_Automation(TypedDict):
    Automation: (
        "aws_sdk_ssm.types.automation_execution_preview.AutomationExecutionPreview"
    )


ExecutionPreview: TypeAlias = _ExecutionPreview_Automation


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecutionPreview) -> dict:
    if "Automation" in value:
        import aws_sdk_ssm.types.automation_execution_preview

        return {
            "Automation": aws_sdk_ssm.types.automation_execution_preview.serialize_aws_json_1_1(
                value["Automation"]
            )
        }
    else:
        raise SerializationError("ExecutionPreview: no variant present")


def deserialize_aws_json_1_1(data: dict) -> ExecutionPreview:
    if "Automation" in data:
        import aws_sdk_ssm.types.automation_execution_preview

        return {
            "Automation": aws_sdk_ssm.types.automation_execution_preview.deserialize_aws_json_1_1(
                data["Automation"]
            )
        }
    else:
        raise DeserializationError("ExecutionPreview: no recognized variant key")
