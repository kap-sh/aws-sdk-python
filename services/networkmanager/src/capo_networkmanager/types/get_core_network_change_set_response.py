"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetCoreNetworkChangeSetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.core_network_change_list
    import capo_networkmanager.types.next_token


class GetCoreNetworkChangeSetResponse(TypedDict, closed=True):
    core_network_changes: NotRequired[
        "capo_networkmanager.types.core_network_change_list.CoreNetworkChangeList"
    ]
    """<p>Describes a core network changes.</p>"""
    next_token: NotRequired["capo_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCoreNetworkChangeSetResponse) -> dict:
    out: dict = {}
    if "core_network_changes" in value:
        import capo_networkmanager.types.core_network_change_list

        out["CoreNetworkChanges"] = (
            capo_networkmanager.types.core_network_change_list.serialize_json(
                value["core_network_changes"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetCoreNetworkChangeSetResponse:
    out: GetCoreNetworkChangeSetResponse = {}  # type: ignore[typeddict-item]
    if "CoreNetworkChanges" in data:
        import capo_networkmanager.types.core_network_change_list

        out["core_network_changes"] = (
            capo_networkmanager.types.core_network_change_list.deserialize_json(
                data["CoreNetworkChanges"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
