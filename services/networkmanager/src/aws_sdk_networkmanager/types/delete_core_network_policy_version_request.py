"""Generated from Smithy shape ``com.amazonaws.networkmanager#DeleteCoreNetworkPolicyVersionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.core_network_id
    import aws_sdk_networkmanager.types.integer


class DeleteCoreNetworkPolicyVersionRequest(TypedDict):
    core_network_id: "aws_sdk_networkmanager.types.core_network_id.CoreNetworkId"
    """<p>The ID of a core network for the deleted policy.</p>"""
    policy_version_id: "aws_sdk_networkmanager.types.integer.Integer"
    """<p>The version ID of the deleted policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCoreNetworkPolicyVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteCoreNetworkPolicyVersionRequest:
    out: DeleteCoreNetworkPolicyVersionRequest = {}  # type: ignore[typeddict-item]
    return out
