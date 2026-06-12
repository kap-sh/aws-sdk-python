"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetNetworkResourceRelationshipsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.next_token
    import aws_sdk_networkmanager.types.relationship_list


class GetNetworkResourceRelationshipsResponse(TypedDict):
    relationships: NotRequired[
        "aws_sdk_networkmanager.types.relationship_list.RelationshipList"
    ]
    """<p>The resource relationships.</p>"""
    next_token: NotRequired["aws_sdk_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetNetworkResourceRelationshipsResponse) -> dict:
    out: dict = {}
    if "relationships" in value:
        import aws_sdk_networkmanager.types.relationship_list

        out["Relationships"] = (
            aws_sdk_networkmanager.types.relationship_list.serialize_json(
                value["relationships"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetNetworkResourceRelationshipsResponse:
    out: GetNetworkResourceRelationshipsResponse = {}  # type: ignore[typeddict-item]
    if "Relationships" in data:
        import aws_sdk_networkmanager.types.relationship_list

        out["relationships"] = (
            aws_sdk_networkmanager.types.relationship_list.deserialize_json(
                data["Relationships"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
