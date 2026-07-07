"""Generated from Smithy shape ``com.amazonaws.codecatalyst#ListDevEnvironmentSessionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codecatalyst.types.name_string
    import aws_sdk_codecatalyst.types.uuid


class ListDevEnvironmentSessionsRequest(TypedDict, closed=True):
    space_name: "aws_sdk_codecatalyst.types.name_string.NameString"
    """<p>The name of the space.</p>"""
    project_name: "aws_sdk_codecatalyst.types.name_string.NameString"
    """<p>The name of the project in the space.</p>"""
    dev_environment_id: "aws_sdk_codecatalyst.types.uuid.Uuid"
    """<p>The system-generated unique ID of the Dev Environment.</p>"""
    next_token: NotRequired["str"]
    """<p>A token returned from a call to this API to indicate the next batch of results to return, if any.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to show in a single call to this API. If the number of results is larger than the number you specified, the response will include a <code>NextToken</code> element, which you can use to obtain additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDevEnvironmentSessionsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListDevEnvironmentSessionsRequest:
    out: ListDevEnvironmentSessionsRequest = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
