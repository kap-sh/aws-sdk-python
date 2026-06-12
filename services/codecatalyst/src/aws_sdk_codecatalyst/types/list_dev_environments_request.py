"""Generated from Smithy shape ``com.amazonaws.codecatalyst#ListDevEnvironmentsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codecatalyst.types.filters
    import aws_sdk_codecatalyst.types.name_string


class ListDevEnvironmentsRequest(TypedDict):
    space_name: "aws_sdk_codecatalyst.types.name_string.NameString"
    """<p>The name of the space.</p>"""
    project_name: NotRequired["aws_sdk_codecatalyst.types.name_string.NameString"]
    """<p>The name of the project in the space.</p>"""
    filters: NotRequired["aws_sdk_codecatalyst.types.filters.Filters"]
    """<p>Information about filters to apply to narrow the results returned in the list.</p>"""
    next_token: NotRequired["str"]
    """<p>A token returned from a call to this API to indicate the next batch of results to return, if any.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to show in a single call to this API. If the number of results is larger than the number you specified, the response will include a <code>NextToken</code> element, which you can use to obtain additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDevEnvironmentsRequest) -> dict:
    out: dict = {}
    if "project_name" in value:
        out["projectName"] = value["project_name"]
    if "filters" in value:
        import aws_sdk_codecatalyst.types.filters

        out["filters"] = aws_sdk_codecatalyst.types.filters.serialize_json(
            value["filters"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListDevEnvironmentsRequest:
    out: ListDevEnvironmentsRequest = {}  # type: ignore[typeddict-item]
    if "projectName" in data:
        out["project_name"] = data["projectName"]
    if "filters" in data:
        import aws_sdk_codecatalyst.types.filters

        out["filters"] = aws_sdk_codecatalyst.types.filters.deserialize_json(
            data["filters"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
