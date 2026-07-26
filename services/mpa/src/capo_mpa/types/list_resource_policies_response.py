"""Generated from Smithy shape ``com.amazonaws.mpa#ListResourcePoliciesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mpa.types.list_resource_policies_response_resource_policies
    import capo_mpa.types.token


class ListResourcePoliciesResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_mpa.types.token.Token"]
    """<p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a next call to the operation to get more output. You can repeat this until the <code>NextToken</code> response element returns <code>null</code>.</p>"""
    resource_policies: NotRequired[
        "capo_mpa.types.list_resource_policies_response_resource_policies.ListResourcePoliciesResponseResourcePolicies"
    ]
    """<p>An array of <code>ListResourcePoliciesResponseResourcePolicy</code> objects. Contains details about the policy for the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListResourcePoliciesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "resource_policies" in value:
        import capo_mpa.types.list_resource_policies_response_resource_policies

        out["ResourcePolicies"] = (
            capo_mpa.types.list_resource_policies_response_resource_policies.serialize_json(
                value["resource_policies"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListResourcePoliciesResponse:
    out: ListResourcePoliciesResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ResourcePolicies" in data:
        import capo_mpa.types.list_resource_policies_response_resource_policies

        out["resource_policies"] = (
            capo_mpa.types.list_resource_policies_response_resource_policies.deserialize_json(
                data["ResourcePolicies"]
            )
        )
    return out
