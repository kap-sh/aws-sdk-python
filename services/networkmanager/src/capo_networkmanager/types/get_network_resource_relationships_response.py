"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetNetworkResourceRelationshipsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.next_token
    import capo_networkmanager.types.relationship_list


class GetNetworkResourceRelationshipsResponse(TypedDict, closed=True):
    relationships: NotRequired[
        "capo_networkmanager.types.relationship_list.RelationshipList"
    ]
    """<p>The resource relationships.</p>"""
    next_token: NotRequired["capo_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetNetworkResourceRelationshipsResponse) -> dict:
    out: dict = {}
    if "relationships" in value:
        import capo_networkmanager.types.relationship_list

        out["Relationships"] = (
            capo_networkmanager.types.relationship_list.serialize_json(
                value["relationships"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetNetworkResourceRelationshipsResponse:
    out: GetNetworkResourceRelationshipsResponse = {}  # type: ignore[typeddict-item]
    if "Relationships" in data:
        import capo_networkmanager.types.relationship_list

        out["relationships"] = (
            capo_networkmanager.types.relationship_list.deserialize_json(
                data["Relationships"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
