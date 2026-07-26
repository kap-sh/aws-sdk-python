"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetCoreNetworkPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.core_network_id
    import capo_networkmanager.types.core_network_policy_alias
    import capo_networkmanager.types.integer


class GetCoreNetworkPolicyRequest(TypedDict, closed=True):
    core_network_id: "capo_networkmanager.types.core_network_id.CoreNetworkId"
    """<p>The ID of a core network.</p>"""
    policy_version_id: NotRequired["capo_networkmanager.types.integer.Integer"]
    """<p>The ID of a core network policy version.</p>"""
    alias: NotRequired[
        "capo_networkmanager.types.core_network_policy_alias.CoreNetworkPolicyAlias"
    ]
    """<p>The alias of a core network policy </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCoreNetworkPolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCoreNetworkPolicyRequest:
    out: GetCoreNetworkPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
