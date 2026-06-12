"""Generated from Smithy shape ``com.amazonaws.sesv2#ListReputationEntitiesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.next_token
    import aws_sdk_sesv2.types.reputation_entities_list


class ListReputationEntitiesResponse(TypedDict):
    reputation_entities: NotRequired[
        "aws_sdk_sesv2.types.reputation_entities_list.ReputationEntitiesList"
    ]
    """<p>An array that contains information about the reputation entities in your account.</p>"""
    next_token: NotRequired["aws_sdk_sesv2.types.next_token.NextToken"]
    """<p>A token that indicates that there are additional reputation entities to list. To view additional reputation entities, issue another request to <code>ListReputationEntities</code>, and pass this token in the <code>NextToken</code> parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListReputationEntitiesResponse) -> dict:
    out: dict = {}
    if "reputation_entities" in value:
        import aws_sdk_sesv2.types.reputation_entities_list

        out["ReputationEntities"] = (
            aws_sdk_sesv2.types.reputation_entities_list.serialize_json(
                value["reputation_entities"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListReputationEntitiesResponse:
    out: ListReputationEntitiesResponse = {}  # type: ignore[typeddict-item]
    if "ReputationEntities" in data:
        import aws_sdk_sesv2.types.reputation_entities_list

        out["reputation_entities"] = (
            aws_sdk_sesv2.types.reputation_entities_list.deserialize_json(
                data["ReputationEntities"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
