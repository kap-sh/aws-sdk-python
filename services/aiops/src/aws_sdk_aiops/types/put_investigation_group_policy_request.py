"""Generated from Smithy shape ``com.amazonaws.aiops#PutInvestigationGroupPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_aiops.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_aiops.types.investigation_group_identifier
    import aws_sdk_aiops.types.investigation_group_policy_document


class PutInvestigationGroupPolicyRequest(TypedDict, closed=True):
    identifier: "aws_sdk_aiops.types.investigation_group_identifier.InvestigationGroupIdentifier"
    """<p>Specify either the name or the ARN of the investigation group that you want to assign the policy to.</p>"""
    policy: "aws_sdk_aiops.types.investigation_group_policy_document.InvestigationGroupPolicyDocument"
    """<p>The policy, in JSON format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutInvestigationGroupPolicyRequest) -> dict:
    out: dict = {}
    out["policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> PutInvestigationGroupPolicyRequest:
    out: PutInvestigationGroupPolicyRequest = {}  # type: ignore[typeddict-item]
    if "policy" in data:
        out["policy"] = data["policy"]
    else:
        raise DeserializationError("PutInvestigationGroupPolicyRequest.policy required")
    return out
