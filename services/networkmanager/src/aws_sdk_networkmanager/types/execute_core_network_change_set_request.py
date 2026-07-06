"""Generated from Smithy shape ``com.amazonaws.networkmanager#ExecuteCoreNetworkChangeSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.core_network_id
    import aws_sdk_networkmanager.types.integer


class ExecuteCoreNetworkChangeSetRequest(TypedDict, closed=True):
    core_network_id: "aws_sdk_networkmanager.types.core_network_id.CoreNetworkId"
    """<p>The ID of a core network.</p>"""
    policy_version_id: "aws_sdk_networkmanager.types.integer.Integer"
    """<p>The ID of the policy version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecuteCoreNetworkChangeSetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ExecuteCoreNetworkChangeSetRequest:
    out: ExecuteCoreNetworkChangeSetRequest = {}  # type: ignore[typeddict-item]
    return out
