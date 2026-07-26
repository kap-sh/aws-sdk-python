"""Generated from Smithy shape ``com.amazonaws.emr#DescribeJobFlowsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.date
    import capo_emr.types.job_flow_execution_state_list
    import capo_emr.types.xml_string_list


class DescribeJobFlowsInput(TypedDict, closed=True):
    created_after: NotRequired["capo_emr.types.date.Date"]
    """<p>Return only job flows created after this date and time.</p>"""
    created_before: NotRequired["capo_emr.types.date.Date"]
    """<p>Return only job flows created before this date and time.</p>"""
    job_flow_ids: NotRequired["capo_emr.types.xml_string_list.XmlStringList"]
    """<p>Return only job flows whose job flow ID is contained in this list.</p>"""
    job_flow_states: NotRequired[
        "capo_emr.types.job_flow_execution_state_list.JobFlowExecutionStateList"
    ]
    """<p>Return only job flows whose state is contained in this list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeJobFlowsInput) -> dict:
    out: dict = {}
    if "created_after" in value:
        import capo_emr.types.date

        out["CreatedAfter"] = capo_emr.types.date.serialize_aws_json_1_1(
            value["created_after"]
        )
    if "created_before" in value:
        import capo_emr.types.date

        out["CreatedBefore"] = capo_emr.types.date.serialize_aws_json_1_1(
            value["created_before"]
        )
    if "job_flow_ids" in value:
        import capo_emr.types.xml_string_list

        out["JobFlowIds"] = capo_emr.types.xml_string_list.serialize_aws_json_1_1(
            value["job_flow_ids"]
        )
    if "job_flow_states" in value:
        import capo_emr.types.job_flow_execution_state_list

        out["JobFlowStates"] = (
            capo_emr.types.job_flow_execution_state_list.serialize_aws_json_1_1(
                value["job_flow_states"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeJobFlowsInput:
    out: DescribeJobFlowsInput = {}  # type: ignore[typeddict-item]
    if "CreatedAfter" in data:
        import capo_emr.types.date

        out["created_after"] = capo_emr.types.date.deserialize_aws_json_1_1(
            data["CreatedAfter"]
        )
    if "CreatedBefore" in data:
        import capo_emr.types.date

        out["created_before"] = capo_emr.types.date.deserialize_aws_json_1_1(
            data["CreatedBefore"]
        )
    if "JobFlowIds" in data:
        import capo_emr.types.xml_string_list

        out["job_flow_ids"] = capo_emr.types.xml_string_list.deserialize_aws_json_1_1(
            data["JobFlowIds"]
        )
    if "JobFlowStates" in data:
        import capo_emr.types.job_flow_execution_state_list

        out["job_flow_states"] = (
            capo_emr.types.job_flow_execution_state_list.deserialize_aws_json_1_1(
                data["JobFlowStates"]
            )
        )
    return out
