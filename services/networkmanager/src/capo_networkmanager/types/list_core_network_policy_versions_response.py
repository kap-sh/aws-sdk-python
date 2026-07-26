"""Generated from Smithy shape ``com.amazonaws.networkmanager#ListCoreNetworkPolicyVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.core_network_policy_version_list
    import capo_networkmanager.types.next_token


class ListCoreNetworkPolicyVersionsResponse(TypedDict, closed=True):
    core_network_policy_versions: NotRequired[
        "capo_networkmanager.types.core_network_policy_version_list.CoreNetworkPolicyVersionList"
    ]
    """<p>Describes core network policy versions.</p>"""
    next_token: NotRequired["capo_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCoreNetworkPolicyVersionsResponse) -> dict:
    out: dict = {}
    if "core_network_policy_versions" in value:
        import capo_networkmanager.types.core_network_policy_version_list

        out["CoreNetworkPolicyVersions"] = (
            capo_networkmanager.types.core_network_policy_version_list.serialize_json(
                value["core_network_policy_versions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCoreNetworkPolicyVersionsResponse:
    out: ListCoreNetworkPolicyVersionsResponse = {}  # type: ignore[typeddict-item]
    if "CoreNetworkPolicyVersions" in data:
        import capo_networkmanager.types.core_network_policy_version_list

        out["core_network_policy_versions"] = (
            capo_networkmanager.types.core_network_policy_version_list.deserialize_json(
                data["CoreNetworkPolicyVersions"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
