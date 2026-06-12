"""Generated from Smithy shape ``com.amazonaws.configservice#RemediationExecutionSteps``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_config_service.types.remediation_execution_step

RemediationExecutionSteps: TypeAlias = list[
    "aws_sdk_config_service.types.remediation_execution_step.RemediationExecutionStep"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemediationExecutionSteps) -> list:
    import aws_sdk_config_service.types.remediation_execution_step

    out: list = []
    for item in value:
        out.append(
            aws_sdk_config_service.types.remediation_execution_step.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RemediationExecutionSteps:
    import aws_sdk_config_service.types.remediation_execution_step

    out: RemediationExecutionSteps = []
    for item in data:
        out.append(
            aws_sdk_config_service.types.remediation_execution_step.deserialize_aws_json_1_1(
                item
            )
        )
    return out
