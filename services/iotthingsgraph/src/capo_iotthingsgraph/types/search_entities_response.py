"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#SearchEntitiesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotthingsgraph.types.entity_descriptions
    import capo_iotthingsgraph.types.next_token


class SearchEntitiesResponse(TypedDict, closed=True):
    descriptions: NotRequired[
        "capo_iotthingsgraph.types.entity_descriptions.EntityDescriptions"
    ]
    """<p>An array of descriptions for each entity returned in the search result.</p>"""
    next_token: NotRequired["capo_iotthingsgraph.types.next_token.NextToken"]
    """<p>The string to specify as <code>nextToken</code> when you request the next page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchEntitiesResponse) -> dict:
    out: dict = {}
    if "descriptions" in value:
        import capo_iotthingsgraph.types.entity_descriptions

        out["descriptions"] = (
            capo_iotthingsgraph.types.entity_descriptions.serialize_aws_json_1_1(
                value["descriptions"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SearchEntitiesResponse:
    out: SearchEntitiesResponse = {}  # type: ignore[typeddict-item]
    if "descriptions" in data:
        import capo_iotthingsgraph.types.entity_descriptions

        out["descriptions"] = (
            capo_iotthingsgraph.types.entity_descriptions.deserialize_aws_json_1_1(
                data["descriptions"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
