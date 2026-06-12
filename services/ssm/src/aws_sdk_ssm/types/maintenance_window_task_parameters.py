"""Generated from Smithy shape ``com.amazonaws.ssm#MaintenanceWindowTaskParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.maintenance_window_task_parameter_name
    import aws_sdk_ssm.types.maintenance_window_task_parameter_value_expression

MaintenanceWindowTaskParameters: TypeAlias = dict[
    "aws_sdk_ssm.types.maintenance_window_task_parameter_name.MaintenanceWindowTaskParameterName",
    "aws_sdk_ssm.types.maintenance_window_task_parameter_value_expression.MaintenanceWindowTaskParameterValueExpression",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: MaintenanceWindowTaskParameters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_ssm.types.maintenance_window_task_parameter_value_expression

        out[key] = (
            aws_sdk_ssm.types.maintenance_window_task_parameter_value_expression.serialize_aws_json_1_1(
                value
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MaintenanceWindowTaskParameters:
    out: MaintenanceWindowTaskParameters = {}
    for key, value in data.items():
        import aws_sdk_ssm.types.maintenance_window_task_parameter_value_expression

        out[key] = (
            aws_sdk_ssm.types.maintenance_window_task_parameter_value_expression.deserialize_aws_json_1_1(
                value
            )
        )
    return out
