"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#GetResourcePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.resource_policy_json


class GetResourcePolicyResponse(TypedDict, closed=True):
    policy: NotRequired[
        "capo_marketplace_catalog.types.resource_policy_json.ResourcePolicyJson"
    ]
    """<p>The policy document to set; formatted in JSON.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourcePolicyResponse) -> dict:
    out: dict = {}
    if "policy" in value:
        out["Policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> GetResourcePolicyResponse:
    out: GetResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    if "Policy" in data:
        out["policy"] = data["Policy"]
    return out
