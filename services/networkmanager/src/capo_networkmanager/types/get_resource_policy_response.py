"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetResourcePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.synthesized_json_resource_policy_document


class GetResourcePolicyResponse(TypedDict, closed=True):
    policy_document: NotRequired[
        "capo_networkmanager.types.synthesized_json_resource_policy_document.SynthesizedJsonResourcePolicyDocument"
    ]
    """<p>The resource policy document.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourcePolicyResponse) -> dict:
    out: dict = {}
    if "policy_document" in value:
        out["PolicyDocument"] = value["policy_document"]
    return out


def deserialize_json(data: dict) -> GetResourcePolicyResponse:
    out: GetResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    if "PolicyDocument" in data:
        out["policy_document"] = data["PolicyDocument"]
    return out
