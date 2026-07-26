"""Generated from Smithy shape ``com.amazonaws.ram#GetResourcePoliciesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ram.types.policy_list
    import capo_ram.types.string


class GetResourcePoliciesResponse(TypedDict, closed=True):
    policies: NotRequired["capo_ram.types.policy_list.PolicyList"]
    """<p>An array of resource policy documents in JSON format.</p>"""
    next_token: NotRequired["capo_ram.types.string.String"]
    """<p>If present, this value indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>. This indicates that this is the last page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourcePoliciesResponse) -> dict:
    out: dict = {}
    if "policies" in value:
        import capo_ram.types.policy_list

        out["policies"] = capo_ram.types.policy_list.serialize_json(value["policies"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetResourcePoliciesResponse:
    out: GetResourcePoliciesResponse = {}  # type: ignore[typeddict-item]
    if "policies" in data:
        import capo_ram.types.policy_list

        out["policies"] = capo_ram.types.policy_list.deserialize_json(data["policies"])
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
