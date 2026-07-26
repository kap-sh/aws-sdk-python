"""Generated from Smithy shape ``com.amazonaws.networkmanager#ListCoreNetworkPrefixListAssociationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.next_token
    import capo_networkmanager.types.prefix_list_association_list


class ListCoreNetworkPrefixListAssociationsResponse(TypedDict, closed=True):
    prefix_list_associations: NotRequired[
        "capo_networkmanager.types.prefix_list_association_list.PrefixListAssociationList"
    ]
    """<p>The list of prefix list associations for the core network.</p>"""
    next_token: NotRequired["capo_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCoreNetworkPrefixListAssociationsResponse) -> dict:
    out: dict = {}
    if "prefix_list_associations" in value:
        import capo_networkmanager.types.prefix_list_association_list

        out["PrefixListAssociations"] = (
            capo_networkmanager.types.prefix_list_association_list.serialize_json(
                value["prefix_list_associations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCoreNetworkPrefixListAssociationsResponse:
    out: ListCoreNetworkPrefixListAssociationsResponse = {}  # type: ignore[typeddict-item]
    if "PrefixListAssociations" in data:
        import capo_networkmanager.types.prefix_list_association_list

        out["prefix_list_associations"] = (
            capo_networkmanager.types.prefix_list_association_list.deserialize_json(
                data["PrefixListAssociations"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
