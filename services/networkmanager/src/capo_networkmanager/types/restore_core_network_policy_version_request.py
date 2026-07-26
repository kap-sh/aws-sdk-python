"""Generated from Smithy shape ``com.amazonaws.networkmanager#RestoreCoreNetworkPolicyVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.core_network_id
    import capo_networkmanager.types.integer


class RestoreCoreNetworkPolicyVersionRequest(TypedDict, closed=True):
    core_network_id: "capo_networkmanager.types.core_network_id.CoreNetworkId"
    """<p>The ID of a core network.</p>"""
    policy_version_id: "capo_networkmanager.types.integer.Integer"
    """<p>The ID of the policy version to restore.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RestoreCoreNetworkPolicyVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RestoreCoreNetworkPolicyVersionRequest:
    out: RestoreCoreNetworkPolicyVersionRequest = {}  # type: ignore[typeddict-item]
    return out
