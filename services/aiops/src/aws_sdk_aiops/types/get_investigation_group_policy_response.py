"""Generated from Smithy shape ``com.amazonaws.aiops#GetInvestigationGroupPolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_aiops.types.investigation_group_arn
    import aws_sdk_aiops.types.investigation_group_policy_document


class GetInvestigationGroupPolicyResponse(TypedDict):
    investigation_group_arn: NotRequired[
        "aws_sdk_aiops.types.investigation_group_arn.InvestigationGroupArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the investigation group that you want to view the policy of.</p>"""
    policy: NotRequired[
        "aws_sdk_aiops.types.investigation_group_policy_document.InvestigationGroupPolicyDocument"
    ]
    """<p>The policy, in JSON format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetInvestigationGroupPolicyResponse) -> dict:
    out: dict = {}
    if "investigation_group_arn" in value:
        out["investigationGroupArn"] = value["investigation_group_arn"]
    if "policy" in value:
        out["policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> GetInvestigationGroupPolicyResponse:
    out: GetInvestigationGroupPolicyResponse = {}  # type: ignore[typeddict-item]
    if "investigationGroupArn" in data:
        out["investigation_group_arn"] = data["investigationGroupArn"]
    if "policy" in data:
        out["policy"] = data["policy"]
    return out
