"""Generated from Smithy shape ``com.amazonaws.ssm#ExecutionInputs``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_ssm.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.automation_execution_inputs


class _ExecutionInputs_Automation(TypedDict, closed=True):
    Automation: (
        "aws_sdk_ssm.types.automation_execution_inputs.AutomationExecutionInputs"
    )


ExecutionInputs: TypeAlias = _ExecutionInputs_Automation


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecutionInputs) -> dict:
    if "Automation" in value:
        import aws_sdk_ssm.types.automation_execution_inputs

        return {
            "Automation": aws_sdk_ssm.types.automation_execution_inputs.serialize_aws_json_1_1(
                value["Automation"]
            )
        }
    else:
        raise SerializationError("ExecutionInputs: no variant present")


def deserialize_aws_json_1_1(data: dict) -> ExecutionInputs:
    if "Automation" in data:
        import aws_sdk_ssm.types.automation_execution_inputs

        return {
            "Automation": aws_sdk_ssm.types.automation_execution_inputs.deserialize_aws_json_1_1(
                data["Automation"]
            )
        }
    else:
        raise DeserializationError("ExecutionInputs: no recognized variant key")
