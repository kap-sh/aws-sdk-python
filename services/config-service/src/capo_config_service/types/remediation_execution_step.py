"""Generated from Smithy shape ``com.amazonaws.configservice#RemediationExecutionStep``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.date
    import capo_config_service.types.remediation_execution_step_state
    import capo_config_service.types.string


class RemediationExecutionStep(TypedDict, closed=True):
    name: NotRequired["capo_config_service.types.string.String"]
    """<p>The details of the step.</p>"""
    state: NotRequired[
        "capo_config_service.types.remediation_execution_step_state.RemediationExecutionStepState"
    ]
    """<p>The valid status of the step.</p>"""
    error_message: NotRequired["capo_config_service.types.string.String"]
    """<p>An error message if the step was interrupted during execution.</p>"""
    start_time: NotRequired["capo_config_service.types.date.Date"]
    """<p>The time when the step started.</p>"""
    stop_time: NotRequired["capo_config_service.types.date.Date"]
    """<p>The time when the step stopped.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemediationExecutionStep) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "state" in value:
        import capo_config_service.types.remediation_execution_step_state

        out["State"] = (
            capo_config_service.types.remediation_execution_step_state.serialize_aws_json_1_1(
                value["state"]
            )
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "start_time" in value:
        import capo_config_service.types.date

        out["StartTime"] = capo_config_service.types.date.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "stop_time" in value:
        import capo_config_service.types.date

        out["StopTime"] = capo_config_service.types.date.serialize_aws_json_1_1(
            value["stop_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RemediationExecutionStep:
    out: RemediationExecutionStep = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "State" in data:
        import capo_config_service.types.remediation_execution_step_state

        out["state"] = (
            capo_config_service.types.remediation_execution_step_state.deserialize_aws_json_1_1(
                data["State"]
            )
        )
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    if "StartTime" in data:
        import capo_config_service.types.date

        out["start_time"] = capo_config_service.types.date.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if "StopTime" in data:
        import capo_config_service.types.date

        out["stop_time"] = capo_config_service.types.date.deserialize_aws_json_1_1(
            data["StopTime"]
        )
    return out
