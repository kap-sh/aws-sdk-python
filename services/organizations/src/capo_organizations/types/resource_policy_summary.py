"""Generated from Smithy shape ``com.amazonaws.organizations#ResourcePolicySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_organizations.types.resource_policy_arn
    import capo_organizations.types.resource_policy_id


class ResourcePolicySummary(TypedDict, closed=True):
    id: NotRequired["capo_organizations.types.resource_policy_id.ResourcePolicyId"]
    """<p>The unique identifier (ID) of the resource policy.</p>"""
    arn: NotRequired["capo_organizations.types.resource_policy_arn.ResourcePolicyArn"]
    """<p>The Amazon Resource Name (ARN) of the resource policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourcePolicySummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourcePolicySummary:
    out: ResourcePolicySummary = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
