"""Generated from Smithy shape ``com.amazonaws.networkmanager#RestoreCoreNetworkPolicyVersionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.core_network_policy


class RestoreCoreNetworkPolicyVersionResponse(TypedDict):
    core_network_policy: NotRequired[
        "aws_sdk_networkmanager.types.core_network_policy.CoreNetworkPolicy"
    ]
    """<p>Describes the restored core network policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RestoreCoreNetworkPolicyVersionResponse) -> dict:
    out: dict = {}
    if "core_network_policy" in value:
        import aws_sdk_networkmanager.types.core_network_policy

        out["CoreNetworkPolicy"] = (
            aws_sdk_networkmanager.types.core_network_policy.serialize_json(
                value["core_network_policy"]
            )
        )
    return out


def deserialize_json(data: dict) -> RestoreCoreNetworkPolicyVersionResponse:
    out: RestoreCoreNetworkPolicyVersionResponse = {}  # type: ignore[typeddict-item]
    if "CoreNetworkPolicy" in data:
        import aws_sdk_networkmanager.types.core_network_policy

        out["core_network_policy"] = (
            aws_sdk_networkmanager.types.core_network_policy.deserialize_json(
                data["CoreNetworkPolicy"]
            )
        )
    return out
