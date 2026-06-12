"""Generated from Smithy shape ``com.amazonaws.ssm#MaintenanceWindowTaskInvocationParameters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.maintenance_window_automation_parameters
    import aws_sdk_ssm.types.maintenance_window_lambda_parameters
    import aws_sdk_ssm.types.maintenance_window_run_command_parameters
    import aws_sdk_ssm.types.maintenance_window_step_functions_parameters

MaintenanceWindowTaskInvocationParameters = TypedDict(
    "MaintenanceWindowTaskInvocationParameters",
    {
        "run_command": NotRequired[
            "aws_sdk_ssm.types.maintenance_window_run_command_parameters.MaintenanceWindowRunCommandParameters"
        ],
        "automation": NotRequired[
            "aws_sdk_ssm.types.maintenance_window_automation_parameters.MaintenanceWindowAutomationParameters"
        ],
        "step_functions": NotRequired[
            "aws_sdk_ssm.types.maintenance_window_step_functions_parameters.MaintenanceWindowStepFunctionsParameters"
        ],
        "lambda": NotRequired[
            "aws_sdk_ssm.types.maintenance_window_lambda_parameters.MaintenanceWindowLambdaParameters"
        ],
    },
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MaintenanceWindowTaskInvocationParameters) -> dict:
    out: dict = {}
    if "run_command" in value:
        import aws_sdk_ssm.types.maintenance_window_run_command_parameters

        out["RunCommand"] = (
            aws_sdk_ssm.types.maintenance_window_run_command_parameters.serialize_aws_json_1_1(
                value["run_command"]
            )
        )
    if "automation" in value:
        import aws_sdk_ssm.types.maintenance_window_automation_parameters

        out["Automation"] = (
            aws_sdk_ssm.types.maintenance_window_automation_parameters.serialize_aws_json_1_1(
                value["automation"]
            )
        )
    if "step_functions" in value:
        import aws_sdk_ssm.types.maintenance_window_step_functions_parameters

        out["StepFunctions"] = (
            aws_sdk_ssm.types.maintenance_window_step_functions_parameters.serialize_aws_json_1_1(
                value["step_functions"]
            )
        )
    if "lambda" in value:
        import aws_sdk_ssm.types.maintenance_window_lambda_parameters

        out["Lambda"] = (
            aws_sdk_ssm.types.maintenance_window_lambda_parameters.serialize_aws_json_1_1(
                value["lambda"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MaintenanceWindowTaskInvocationParameters:
    out: MaintenanceWindowTaskInvocationParameters = {}  # type: ignore[typeddict-item]
    if "RunCommand" in data:
        import aws_sdk_ssm.types.maintenance_window_run_command_parameters

        out["run_command"] = (
            aws_sdk_ssm.types.maintenance_window_run_command_parameters.deserialize_aws_json_1_1(
                data["RunCommand"]
            )
        )
    if "Automation" in data:
        import aws_sdk_ssm.types.maintenance_window_automation_parameters

        out["automation"] = (
            aws_sdk_ssm.types.maintenance_window_automation_parameters.deserialize_aws_json_1_1(
                data["Automation"]
            )
        )
    if "StepFunctions" in data:
        import aws_sdk_ssm.types.maintenance_window_step_functions_parameters

        out["step_functions"] = (
            aws_sdk_ssm.types.maintenance_window_step_functions_parameters.deserialize_aws_json_1_1(
                data["StepFunctions"]
            )
        )
    if "Lambda" in data:
        import aws_sdk_ssm.types.maintenance_window_lambda_parameters

        out["lambda"] = (
            aws_sdk_ssm.types.maintenance_window_lambda_parameters.deserialize_aws_json_1_1(
                data["Lambda"]
            )
        )
    return out
