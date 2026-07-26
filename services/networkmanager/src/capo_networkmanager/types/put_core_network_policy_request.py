"""Generated from Smithy shape ``com.amazonaws.networkmanager#PutCoreNetworkPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_networkmanager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_networkmanager.types.client_token
    import capo_networkmanager.types.constrained_string
    import capo_networkmanager.types.core_network_id
    import capo_networkmanager.types.integer
    import capo_networkmanager.types.synthesized_json_core_network_policy_document


class PutCoreNetworkPolicyRequest(TypedDict, closed=True):
    core_network_id: "capo_networkmanager.types.core_network_id.CoreNetworkId"
    """<p>The ID of a core network.</p>"""
    policy_document: "capo_networkmanager.types.synthesized_json_core_network_policy_document.SynthesizedJsonCoreNetworkPolicyDocument"
    """<p>The policy document.</p>"""
    description: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>a core network policy description.</p>"""
    latest_version_id: NotRequired["capo_networkmanager.types.integer.Integer"]
    """<p>The ID of a core network policy. </p>"""
    client_token: NotRequired["capo_networkmanager.types.client_token.ClientToken"]
    """<p>The client token associated with the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutCoreNetworkPolicyRequest) -> dict:
    out: dict = {}
    out["PolicyDocument"] = value["policy_document"]
    if "description" in value:
        out["Description"] = value["description"]
    if "latest_version_id" in value:
        out["LatestVersionId"] = value["latest_version_id"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> PutCoreNetworkPolicyRequest:
    out: PutCoreNetworkPolicyRequest = {}  # type: ignore[typeddict-item]
    if "PolicyDocument" in data:
        out["policy_document"] = data["PolicyDocument"]
    else:
        raise DeserializationError(
            "PutCoreNetworkPolicyRequest.policy_document required"
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "LatestVersionId" in data:
        out["latest_version_id"] = data["LatestVersionId"]
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out
