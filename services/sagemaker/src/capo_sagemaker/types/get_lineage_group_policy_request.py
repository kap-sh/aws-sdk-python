"""Generated from Smithy shape ``com.amazonaws.sagemaker#GetLineageGroupPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.lineage_group_name_or_arn


class GetLineageGroupPolicyRequest(TypedDict, closed=True):
    lineage_group_name: NotRequired[
        "capo_sagemaker.types.lineage_group_name_or_arn.LineageGroupNameOrArn"
    ]
    """<p>The name or Amazon Resource Name (ARN) of the lineage group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetLineageGroupPolicyRequest) -> dict:
    out: dict = {}
    if "lineage_group_name" in value:
        out["LineageGroupName"] = value["lineage_group_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetLineageGroupPolicyRequest:
    out: GetLineageGroupPolicyRequest = {}  # type: ignore[typeddict-item]
    if "LineageGroupName" in data:
        out["lineage_group_name"] = data["LineageGroupName"]
    return out
