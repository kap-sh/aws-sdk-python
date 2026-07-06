"""Generated from Smithy shape ``com.amazonaws.frauddetector#GetListsMetadataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.lists_metadata_max_results
    import aws_sdk_frauddetector.types.next_token
    import aws_sdk_frauddetector.types.no_dash_identifier


class GetListsMetadataRequest(TypedDict, closed=True):
    name: NotRequired["aws_sdk_frauddetector.types.no_dash_identifier.noDashIdentifier"]
    """<p> The name of the list. </p>"""
    next_token: NotRequired["aws_sdk_frauddetector.types.next_token.nextToken"]
    """<p> The next token for the subsequent request. </p>"""
    max_results: NotRequired[
        "aws_sdk_frauddetector.types.lists_metadata_max_results.ListsMetadataMaxResults"
    ]
    """<p> The maximum number of objects to return for the request. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetListsMetadataRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetListsMetadataRequest:
    out: GetListsMetadataRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
