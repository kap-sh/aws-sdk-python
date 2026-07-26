"""Generated from Smithy shape ``com.amazonaws.ssm#MaintenanceWindowExecutionTaskInvocationIdentityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.maintenance_window_execution_task_invocation_identity

MaintenanceWindowExecutionTaskInvocationIdentityList: TypeAlias = list[
    "capo_ssm.types.maintenance_window_execution_task_invocation_identity.MaintenanceWindowExecutionTaskInvocationIdentity"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: MaintenanceWindowExecutionTaskInvocationIdentityList,
) -> list:
    import capo_ssm.types.maintenance_window_execution_task_invocation_identity

    out: list = []
    for item in value:
        out.append(
            capo_ssm.types.maintenance_window_execution_task_invocation_identity.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: list,
) -> MaintenanceWindowExecutionTaskInvocationIdentityList:
    import capo_ssm.types.maintenance_window_execution_task_invocation_identity

    out: MaintenanceWindowExecutionTaskInvocationIdentityList = []
    for item in data:
        out.append(
            capo_ssm.types.maintenance_window_execution_task_invocation_identity.deserialize_aws_json_1_1(
                item
            )
        )
    return out
