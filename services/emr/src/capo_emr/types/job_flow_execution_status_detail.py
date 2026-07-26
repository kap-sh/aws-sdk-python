"""Generated from Smithy shape ``com.amazonaws.emr#JobFlowExecutionStatusDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.date
    import capo_emr.types.job_flow_execution_state
    import capo_emr.types.xml_string


class JobFlowExecutionStatusDetail(TypedDict, closed=True):
    state: NotRequired["capo_emr.types.job_flow_execution_state.JobFlowExecutionState"]
    """<p>The state of the job flow.</p>"""
    creation_date_time: NotRequired["capo_emr.types.date.Date"]
    """<p>The creation date and time of the job flow.</p>"""
    start_date_time: NotRequired["capo_emr.types.date.Date"]
    """<p>The start date and time of the job flow.</p>"""
    ready_date_time: NotRequired["capo_emr.types.date.Date"]
    """<p>The date and time when the job flow was ready to start running bootstrap actions.</p>"""
    end_date_time: NotRequired["capo_emr.types.date.Date"]
    """<p>The completion date and time of the job flow.</p>"""
    last_state_change_reason: NotRequired["capo_emr.types.xml_string.XmlString"]
    """<p>Description of the job flow last changed state.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JobFlowExecutionStatusDetail) -> dict:
    out: dict = {}
    if "state" in value:
        import capo_emr.types.job_flow_execution_state

        out["State"] = capo_emr.types.job_flow_execution_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "creation_date_time" in value:
        import capo_emr.types.date

        out["CreationDateTime"] = capo_emr.types.date.serialize_aws_json_1_1(
            value["creation_date_time"]
        )
    if "start_date_time" in value:
        import capo_emr.types.date

        out["StartDateTime"] = capo_emr.types.date.serialize_aws_json_1_1(
            value["start_date_time"]
        )
    if "ready_date_time" in value:
        import capo_emr.types.date

        out["ReadyDateTime"] = capo_emr.types.date.serialize_aws_json_1_1(
            value["ready_date_time"]
        )
    if "end_date_time" in value:
        import capo_emr.types.date

        out["EndDateTime"] = capo_emr.types.date.serialize_aws_json_1_1(
            value["end_date_time"]
        )
    if "last_state_change_reason" in value:
        out["LastStateChangeReason"] = value["last_state_change_reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> JobFlowExecutionStatusDetail:
    out: JobFlowExecutionStatusDetail = {}  # type: ignore[typeddict-item]
    if "State" in data:
        import capo_emr.types.job_flow_execution_state

        out["state"] = capo_emr.types.job_flow_execution_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if "CreationDateTime" in data:
        import capo_emr.types.date

        out["creation_date_time"] = capo_emr.types.date.deserialize_aws_json_1_1(
            data["CreationDateTime"]
        )
    if "StartDateTime" in data:
        import capo_emr.types.date

        out["start_date_time"] = capo_emr.types.date.deserialize_aws_json_1_1(
            data["StartDateTime"]
        )
    if "ReadyDateTime" in data:
        import capo_emr.types.date

        out["ready_date_time"] = capo_emr.types.date.deserialize_aws_json_1_1(
            data["ReadyDateTime"]
        )
    if "EndDateTime" in data:
        import capo_emr.types.date

        out["end_date_time"] = capo_emr.types.date.deserialize_aws_json_1_1(
            data["EndDateTime"]
        )
    if "LastStateChangeReason" in data:
        out["last_state_change_reason"] = data["LastStateChangeReason"]
    return out
