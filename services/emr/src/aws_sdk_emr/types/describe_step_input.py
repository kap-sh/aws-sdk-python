"""Generated from Smithy shape ``com.amazonaws.emr#DescribeStepInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr.types.cluster_id
    import aws_sdk_emr.types.step_id


class DescribeStepInput(TypedDict, closed=True):
    cluster_id: NotRequired["aws_sdk_emr.types.cluster_id.ClusterId"]
    """<p>The identifier of the cluster with steps to describe.</p>"""
    step_id: NotRequired["aws_sdk_emr.types.step_id.StepId"]
    """<p>The identifier of the step to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeStepInput) -> dict:
    out: dict = {}
    if "cluster_id" in value:
        out["ClusterId"] = value["cluster_id"]
    if "step_id" in value:
        out["StepId"] = value["step_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeStepInput:
    out: DescribeStepInput = {}  # type: ignore[typeddict-item]
    if "ClusterId" in data:
        out["cluster_id"] = data["ClusterId"]
    if "StepId" in data:
        out["step_id"] = data["StepId"]
    return out
