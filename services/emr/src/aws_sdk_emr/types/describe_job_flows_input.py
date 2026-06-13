"""Generated from Smithy shape ``com.amazonaws.emr#DescribeJobFlowsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.date
    import aws_sdk_emr.types.job_flow_execution_state_list
    import aws_sdk_emr.types.xml_string_list


class DescribeJobFlowsInput(TypedDict):
    created_after: NotRequired["aws_sdk_emr.types.date.Date"]
    """<p>Return only job flows created after this date and time.</p>"""
    created_before: NotRequired["aws_sdk_emr.types.date.Date"]
    """<p>Return only job flows created before this date and time.</p>"""
    job_flow_ids: NotRequired["aws_sdk_emr.types.xml_string_list.XmlStringList"]
    """<p>Return only job flows whose job flow ID is contained in this list.</p>"""
    job_flow_states: NotRequired[
        "aws_sdk_emr.types.job_flow_execution_state_list.JobFlowExecutionStateList"
    ]
    """<p>Return only job flows whose state is contained in this list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeJobFlowsInput) -> dict:
    out: dict = {}
    if "created_after" in value:
        import aws_sdk_emr.types.date

        out["CreatedAfter"] = aws_sdk_emr.types.date.serialize_aws_json_1_1(
            value["created_after"]
        )
    if "created_before" in value:
        import aws_sdk_emr.types.date

        out["CreatedBefore"] = aws_sdk_emr.types.date.serialize_aws_json_1_1(
            value["created_before"]
        )
    if "job_flow_ids" in value:
        import aws_sdk_emr.types.xml_string_list

        out["JobFlowIds"] = aws_sdk_emr.types.xml_string_list.serialize_aws_json_1_1(
            value["job_flow_ids"]
        )
    if "job_flow_states" in value:
        import aws_sdk_emr.types.job_flow_execution_state_list

        out["JobFlowStates"] = (
            aws_sdk_emr.types.job_flow_execution_state_list.serialize_aws_json_1_1(
                value["job_flow_states"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeJobFlowsInput:
    out: DescribeJobFlowsInput = {}  # type: ignore[typeddict-item]
    if "CreatedAfter" in data:
        import aws_sdk_emr.types.date

        out["created_after"] = aws_sdk_emr.types.date.deserialize_aws_json_1_1(
            data["CreatedAfter"]
        )
    if "CreatedBefore" in data:
        import aws_sdk_emr.types.date

        out["created_before"] = aws_sdk_emr.types.date.deserialize_aws_json_1_1(
            data["CreatedBefore"]
        )
    if "JobFlowIds" in data:
        import aws_sdk_emr.types.xml_string_list

        out["job_flow_ids"] = (
            aws_sdk_emr.types.xml_string_list.deserialize_aws_json_1_1(
                data["JobFlowIds"]
            )
        )
    if "JobFlowStates" in data:
        import aws_sdk_emr.types.job_flow_execution_state_list

        out["job_flow_states"] = (
            aws_sdk_emr.types.job_flow_execution_state_list.deserialize_aws_json_1_1(
                data["JobFlowStates"]
            )
        )
    return out
