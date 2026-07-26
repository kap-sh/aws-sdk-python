"""Generated from Smithy shape ``com.amazonaws.xray#ListResourcePoliciesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.resource_policy_list
    import capo_xray.types.resource_policy_next_token


class ListResourcePoliciesResult(TypedDict, closed=True):
    resource_policies: NotRequired[
        "capo_xray.types.resource_policy_list.ResourcePolicyList"
    ]
    """<p>The list of resource policies in the target Amazon Web Services account.</p>"""
    next_token: NotRequired[
        "capo_xray.types.resource_policy_next_token.ResourcePolicyNextToken"
    ]
    """<p>Pagination token. Not currently supported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListResourcePoliciesResult) -> dict:
    out: dict = {}
    if "resource_policies" in value:
        import capo_xray.types.resource_policy_list

        out["ResourcePolicies"] = capo_xray.types.resource_policy_list.serialize_json(
            value["resource_policies"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListResourcePoliciesResult:
    out: ListResourcePoliciesResult = {}  # type: ignore[typeddict-item]
    if "ResourcePolicies" in data:
        import capo_xray.types.resource_policy_list

        out["resource_policies"] = (
            capo_xray.types.resource_policy_list.deserialize_json(
                data["ResourcePolicies"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
