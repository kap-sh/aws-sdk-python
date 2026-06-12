"""Generated from Smithy shape ``com.amazonaws.aiops#PutInvestigationGroupPolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_aiops.types.investigation_group_arn


class PutInvestigationGroupPolicyResponse(TypedDict):
    investigation_group_arn: NotRequired[
        "aws_sdk_aiops.types.investigation_group_arn.InvestigationGroupArn"
    ]
    """<p>The ARN of the investigation group that will use this policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutInvestigationGroupPolicyResponse) -> dict:
    out: dict = {}
    if "investigation_group_arn" in value:
        out["investigationGroupArn"] = value["investigation_group_arn"]
    return out


def deserialize_json(data: dict) -> PutInvestigationGroupPolicyResponse:
    out: PutInvestigationGroupPolicyResponse = {}  # type: ignore[typeddict-item]
    if "investigationGroupArn" in data:
        out["investigation_group_arn"] = data["investigationGroupArn"]
    return out
