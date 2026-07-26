"""Generated from Smithy shape ``com.amazonaws.configservice#GetOrganizationCustomRulePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.policy_text


class GetOrganizationCustomRulePolicyResponse(TypedDict, closed=True):
    policy_text: NotRequired["capo_config_service.types.policy_text.PolicyText"]
    """<p>The policy definition containing the logic for your organization Config Custom Policy rule.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetOrganizationCustomRulePolicyResponse) -> dict:
    out: dict = {}
    if "policy_text" in value:
        out["PolicyText"] = value["policy_text"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetOrganizationCustomRulePolicyResponse:
    out: GetOrganizationCustomRulePolicyResponse = {}  # type: ignore[typeddict-item]
    if "PolicyText" in data:
        out["policy_text"] = data["PolicyText"]
    return out
