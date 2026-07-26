"""Generated from Smithy shape ``com.amazonaws.organizations#PutResourcePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_organizations.types.resource_policy


class PutResourcePolicyResponse(TypedDict, closed=True):
    resource_policy: NotRequired[
        "capo_organizations.types.resource_policy.ResourcePolicy"
    ]
    """<p>A structure that contains details about the resource policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutResourcePolicyResponse) -> dict:
    out: dict = {}
    if "resource_policy" in value:
        import capo_organizations.types.resource_policy

        out["ResourcePolicy"] = (
            capo_organizations.types.resource_policy.serialize_aws_json_1_1(
                value["resource_policy"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutResourcePolicyResponse:
    out: PutResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    if "ResourcePolicy" in data:
        import capo_organizations.types.resource_policy

        out["resource_policy"] = (
            capo_organizations.types.resource_policy.deserialize_aws_json_1_1(
                data["ResourcePolicy"]
            )
        )
    return out
