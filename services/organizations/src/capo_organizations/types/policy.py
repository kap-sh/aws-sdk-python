"""Generated from Smithy shape ``com.amazonaws.organizations#Policy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_organizations.types.policy_content
    import capo_organizations.types.policy_summary


class Policy(TypedDict, closed=True):
    policy_summary: NotRequired["capo_organizations.types.policy_summary.PolicySummary"]
    """<p>A structure that contains additional details about the policy.</p>"""
    content: NotRequired["capo_organizations.types.policy_content.PolicyContent"]
    """<p>The text content of the policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Policy) -> dict:
    out: dict = {}
    if "policy_summary" in value:
        import capo_organizations.types.policy_summary

        out["PolicySummary"] = (
            capo_organizations.types.policy_summary.serialize_aws_json_1_1(
                value["policy_summary"]
            )
        )
    if "content" in value:
        out["Content"] = value["content"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Policy:
    out: Policy = {}  # type: ignore[typeddict-item]
    if "PolicySummary" in data:
        import capo_organizations.types.policy_summary

        out["policy_summary"] = (
            capo_organizations.types.policy_summary.deserialize_aws_json_1_1(
                data["PolicySummary"]
            )
        )
    if "Content" in data:
        out["content"] = data["Content"]
    return out
