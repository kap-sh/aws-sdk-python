"""Generated from Smithy shape ``com.amazonaws.emr#RunJobFlowOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.arn_type
    import capo_emr.types.xml_string_max_len256


class RunJobFlowOutput(TypedDict, closed=True):
    job_flow_id: NotRequired["capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>A unique identifier for the job flow.</p>"""
    cluster_arn: NotRequired["capo_emr.types.arn_type.ArnType"]
    """<p>The Amazon Resource Name (ARN) of the cluster.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RunJobFlowOutput) -> dict:
    out: dict = {}
    if "job_flow_id" in value:
        out["JobFlowId"] = value["job_flow_id"]
    if "cluster_arn" in value:
        out["ClusterArn"] = value["cluster_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RunJobFlowOutput:
    out: RunJobFlowOutput = {}  # type: ignore[typeddict-item]
    if "JobFlowId" in data:
        out["job_flow_id"] = data["JobFlowId"]
    if "ClusterArn" in data:
        out["cluster_arn"] = data["ClusterArn"]
    return out
