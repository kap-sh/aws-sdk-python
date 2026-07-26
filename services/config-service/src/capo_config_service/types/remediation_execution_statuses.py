"""Generated from Smithy shape ``com.amazonaws.configservice#RemediationExecutionStatuses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_config_service.types.remediation_execution_status

RemediationExecutionStatuses: TypeAlias = list[
    "capo_config_service.types.remediation_execution_status.RemediationExecutionStatus"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemediationExecutionStatuses) -> list:
    import capo_config_service.types.remediation_execution_status

    out: list = []
    for item in value:
        out.append(
            capo_config_service.types.remediation_execution_status.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RemediationExecutionStatuses:
    import capo_config_service.types.remediation_execution_status

    out: RemediationExecutionStatuses = []
    for item in data:
        out.append(
            capo_config_service.types.remediation_execution_status.deserialize_aws_json_1_1(
                item
            )
        )
    return out
