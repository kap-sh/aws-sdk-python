"""Generated from Smithy shape ``com.amazonaws.emr#StepExecutionStatusDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr.types.date
    import aws_sdk_emr.types.step_execution_state
    import aws_sdk_emr.types.xml_string


class StepExecutionStatusDetail(TypedDict, closed=True):
    state: NotRequired["aws_sdk_emr.types.step_execution_state.StepExecutionState"]
    """<p>The state of the step.</p>"""
    creation_date_time: NotRequired["aws_sdk_emr.types.date.Date"]
    """<p>The creation date and time of the step.</p>"""
    start_date_time: NotRequired["aws_sdk_emr.types.date.Date"]
    """<p>The start date and time of the step.</p>"""
    end_date_time: NotRequired["aws_sdk_emr.types.date.Date"]
    """<p>The completion date and time of the step.</p>"""
    last_state_change_reason: NotRequired["aws_sdk_emr.types.xml_string.XmlString"]
    """<p>A description of the step's current state.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StepExecutionStatusDetail) -> dict:
    out: dict = {}
    if "state" in value:
        import aws_sdk_emr.types.step_execution_state

        out["State"] = aws_sdk_emr.types.step_execution_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "creation_date_time" in value:
        import aws_sdk_emr.types.date

        out["CreationDateTime"] = aws_sdk_emr.types.date.serialize_aws_json_1_1(
            value["creation_date_time"]
        )
    if "start_date_time" in value:
        import aws_sdk_emr.types.date

        out["StartDateTime"] = aws_sdk_emr.types.date.serialize_aws_json_1_1(
            value["start_date_time"]
        )
    if "end_date_time" in value:
        import aws_sdk_emr.types.date

        out["EndDateTime"] = aws_sdk_emr.types.date.serialize_aws_json_1_1(
            value["end_date_time"]
        )
    if "last_state_change_reason" in value:
        out["LastStateChangeReason"] = value["last_state_change_reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StepExecutionStatusDetail:
    out: StepExecutionStatusDetail = {}  # type: ignore[typeddict-item]
    if "State" in data:
        import aws_sdk_emr.types.step_execution_state

        out["state"] = aws_sdk_emr.types.step_execution_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if "CreationDateTime" in data:
        import aws_sdk_emr.types.date

        out["creation_date_time"] = aws_sdk_emr.types.date.deserialize_aws_json_1_1(
            data["CreationDateTime"]
        )
    if "StartDateTime" in data:
        import aws_sdk_emr.types.date

        out["start_date_time"] = aws_sdk_emr.types.date.deserialize_aws_json_1_1(
            data["StartDateTime"]
        )
    if "EndDateTime" in data:
        import aws_sdk_emr.types.date

        out["end_date_time"] = aws_sdk_emr.types.date.deserialize_aws_json_1_1(
            data["EndDateTime"]
        )
    if "LastStateChangeReason" in data:
        out["last_state_change_reason"] = data["LastStateChangeReason"]
    return out
