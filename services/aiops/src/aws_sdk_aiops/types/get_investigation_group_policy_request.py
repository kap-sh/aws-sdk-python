"""Generated from Smithy shape ``com.amazonaws.aiops#GetInvestigationGroupPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_aiops.types.investigation_group_identifier


class GetInvestigationGroupPolicyRequest(TypedDict):
    identifier: "aws_sdk_aiops.types.investigation_group_identifier.InvestigationGroupIdentifier"
    """<p>Specify either the name or the ARN of the investigation group that you want to view the policy of.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetInvestigationGroupPolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetInvestigationGroupPolicyRequest:
    out: GetInvestigationGroupPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
