"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetLinkAssociationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.link_association_list
    import capo_networkmanager.types.next_token


class GetLinkAssociationsResponse(TypedDict, closed=True):
    link_associations: NotRequired[
        "capo_networkmanager.types.link_association_list.LinkAssociationList"
    ]
    """<p>The link associations.</p>"""
    next_token: NotRequired["capo_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLinkAssociationsResponse) -> dict:
    out: dict = {}
    if "link_associations" in value:
        import capo_networkmanager.types.link_association_list

        out["LinkAssociations"] = (
            capo_networkmanager.types.link_association_list.serialize_json(
                value["link_associations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetLinkAssociationsResponse:
    out: GetLinkAssociationsResponse = {}  # type: ignore[typeddict-item]
    if "LinkAssociations" in data:
        import capo_networkmanager.types.link_association_list

        out["link_associations"] = (
            capo_networkmanager.types.link_association_list.deserialize_json(
                data["LinkAssociations"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
