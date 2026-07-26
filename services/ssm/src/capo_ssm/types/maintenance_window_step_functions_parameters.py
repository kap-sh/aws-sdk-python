"""Generated from Smithy shape ``com.amazonaws.ssm#MaintenanceWindowStepFunctionsParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.maintenance_window_step_functions_input
    import capo_ssm.types.maintenance_window_step_functions_name


class MaintenanceWindowStepFunctionsParameters(TypedDict, closed=True):
    input: NotRequired[
        "capo_ssm.types.maintenance_window_step_functions_input.MaintenanceWindowStepFunctionsInput"
    ]
    """<p>The inputs for the <code>STEP_FUNCTIONS</code> task.</p>"""
    name: NotRequired[
        "capo_ssm.types.maintenance_window_step_functions_name.MaintenanceWindowStepFunctionsName"
    ]
    """<p>The name of the <code>STEP_FUNCTIONS</code> task.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MaintenanceWindowStepFunctionsParameters) -> dict:
    out: dict = {}
    if "input" in value:
        out["Input"] = value["input"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MaintenanceWindowStepFunctionsParameters:
    out: MaintenanceWindowStepFunctionsParameters = {}  # type: ignore[typeddict-item]
    if "Input" in data:
        out["input"] = data["Input"]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
