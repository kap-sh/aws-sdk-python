"""Generated from Smithy shape ``com.amazonaws.frauddetector#GetEntityTypesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.entity_types_max_results
    import capo_frauddetector.types.identifier
    import capo_frauddetector.types.string


class GetEntityTypesRequest(TypedDict, closed=True):
    name: NotRequired["capo_frauddetector.types.identifier.identifier"]
    """<p>The name.</p>"""
    next_token: NotRequired["capo_frauddetector.types.string.string"]
    """<p>The next token for the subsequent request.</p>"""
    max_results: NotRequired[
        "capo_frauddetector.types.entity_types_max_results.entityTypesMaxResults"
    ]
    """<p>The maximum number of objects to return for the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetEntityTypesRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetEntityTypesRequest:
    out: GetEntityTypesRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
