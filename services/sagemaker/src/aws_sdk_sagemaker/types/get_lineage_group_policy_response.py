"""Generated from Smithy shape ``com.amazonaws.sagemaker#GetLineageGroupPolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.lineage_group_arn
    import aws_sdk_sagemaker.types.resource_policy_string


class GetLineageGroupPolicyResponse(TypedDict):
    lineage_group_arn: NotRequired[
        "aws_sdk_sagemaker.types.lineage_group_arn.LineageGroupArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the lineage group.</p>"""
    resource_policy: NotRequired[
        "aws_sdk_sagemaker.types.resource_policy_string.ResourcePolicyString"
    ]
    """<p>The resource policy that gives access to the lineage group in another account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetLineageGroupPolicyResponse) -> dict:
    out: dict = {}
    if "lineage_group_arn" in value:
        out["LineageGroupArn"] = value["lineage_group_arn"]
    if "resource_policy" in value:
        out["ResourcePolicy"] = value["resource_policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetLineageGroupPolicyResponse:
    out: GetLineageGroupPolicyResponse = {}  # type: ignore[typeddict-item]
    if "LineageGroupArn" in data:
        out["lineage_group_arn"] = data["LineageGroupArn"]
    if "ResourcePolicy" in data:
        out["resource_policy"] = data["ResourcePolicy"]
    return out
