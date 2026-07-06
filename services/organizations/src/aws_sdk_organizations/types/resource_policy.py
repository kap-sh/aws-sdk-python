"""Generated from Smithy shape ``com.amazonaws.organizations#ResourcePolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_organizations.types.resource_policy_content
    import aws_sdk_organizations.types.resource_policy_summary


class ResourcePolicy(TypedDict, closed=True):
    resource_policy_summary: NotRequired[
        "aws_sdk_organizations.types.resource_policy_summary.ResourcePolicySummary"
    ]
    """<p>A structure that contains resource policy ID and Amazon Resource Name (ARN).</p>"""
    content: NotRequired[
        "aws_sdk_organizations.types.resource_policy_content.ResourcePolicyContent"
    ]
    """<p>The policy text of the resource policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourcePolicy) -> dict:
    out: dict = {}
    if "resource_policy_summary" in value:
        import aws_sdk_organizations.types.resource_policy_summary

        out["ResourcePolicySummary"] = (
            aws_sdk_organizations.types.resource_policy_summary.serialize_aws_json_1_1(
                value["resource_policy_summary"]
            )
        )
    if "content" in value:
        out["Content"] = value["content"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourcePolicy:
    out: ResourcePolicy = {}  # type: ignore[typeddict-item]
    if "ResourcePolicySummary" in data:
        import aws_sdk_organizations.types.resource_policy_summary

        out["resource_policy_summary"] = (
            aws_sdk_organizations.types.resource_policy_summary.deserialize_aws_json_1_1(
                data["ResourcePolicySummary"]
            )
        )
    if "Content" in data:
        out["content"] = data["Content"]
    return out
