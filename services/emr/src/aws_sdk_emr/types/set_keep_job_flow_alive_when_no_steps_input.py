"""Generated from Smithy shape ``com.amazonaws.emr#SetKeepJobFlowAliveWhenNoStepsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.boolean
    import aws_sdk_emr.types.xml_string_list


class SetKeepJobFlowAliveWhenNoStepsInput(TypedDict):
    job_flow_ids: NotRequired["aws_sdk_emr.types.xml_string_list.XmlStringList"]
    """<p>A list of strings that uniquely identify the clusters to protect. This identifier is returned by <a href=\"https://docs.aws.amazon.com/emr/latest/APIReference/API_RunJobFlow.html\">RunJobFlow</a> and can also be obtained from <a href=\"https://docs.aws.amazon.com/emr/latest/APIReference/API_DescribeJobFlows.html\">DescribeJobFlows</a>.</p>"""
    keep_job_flow_alive_when_no_steps: NotRequired["aws_sdk_emr.types.boolean.Boolean"]
    """<p>A Boolean that indicates whether to terminate the cluster after all steps are executed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SetKeepJobFlowAliveWhenNoStepsInput) -> dict:
    out: dict = {}
    if "job_flow_ids" in value:
        import aws_sdk_emr.types.xml_string_list

        out["JobFlowIds"] = aws_sdk_emr.types.xml_string_list.serialize_aws_json_1_1(
            value["job_flow_ids"]
        )
    if "keep_job_flow_alive_when_no_steps" in value:
        out["KeepJobFlowAliveWhenNoSteps"] = value["keep_job_flow_alive_when_no_steps"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SetKeepJobFlowAliveWhenNoStepsInput:
    out: SetKeepJobFlowAliveWhenNoStepsInput = {}  # type: ignore[typeddict-item]
    if "JobFlowIds" in data:
        import aws_sdk_emr.types.xml_string_list

        out["job_flow_ids"] = (
            aws_sdk_emr.types.xml_string_list.deserialize_aws_json_1_1(
                data["JobFlowIds"]
            )
        )
    if "KeepJobFlowAliveWhenNoSteps" in data:
        out["keep_job_flow_alive_when_no_steps"] = data["KeepJobFlowAliveWhenNoSteps"]
    return out
