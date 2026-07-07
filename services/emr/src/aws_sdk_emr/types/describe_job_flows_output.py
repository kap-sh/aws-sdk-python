"""Generated from Smithy shape ``com.amazonaws.emr#DescribeJobFlowsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr.types.job_flow_detail_list


class DescribeJobFlowsOutput(TypedDict, closed=True):
    job_flows: NotRequired["aws_sdk_emr.types.job_flow_detail_list.JobFlowDetailList"]
    """<p>A list of job flows matching the parameters supplied.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeJobFlowsOutput) -> dict:
    out: dict = {}
    if "job_flows" in value:
        import aws_sdk_emr.types.job_flow_detail_list

        out["JobFlows"] = aws_sdk_emr.types.job_flow_detail_list.serialize_aws_json_1_1(
            value["job_flows"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeJobFlowsOutput:
    out: DescribeJobFlowsOutput = {}  # type: ignore[typeddict-item]
    if "JobFlows" in data:
        import aws_sdk_emr.types.job_flow_detail_list

        out["job_flows"] = (
            aws_sdk_emr.types.job_flow_detail_list.deserialize_aws_json_1_1(
                data["JobFlows"]
            )
        )
    return out
