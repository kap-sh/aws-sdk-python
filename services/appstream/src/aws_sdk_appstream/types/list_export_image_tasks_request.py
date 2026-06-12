"""Generated from Smithy shape ``com.amazonaws.appstream#ListExportImageTasksRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appstream.types.filters
    import aws_sdk_appstream.types.max_results
    import aws_sdk_appstream.types.string


class ListExportImageTasksRequest(TypedDict):
    filters: NotRequired["aws_sdk_appstream.types.filters.Filters"]
    """<p>Optional filters to apply when listing export image tasks. Filters help you narrow down the results based on specific criteria.</p>"""
    max_results: NotRequired["aws_sdk_appstream.types.max_results.MaxResults"]
    """<p>The maximum number of export image tasks to return in a single request. The valid range is 1-500, with a default of 50.</p>"""
    next_token: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The pagination token from a previous request. Use this to retrieve the next page of results when there are more tasks than the MaxResults limit.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListExportImageTasksRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import aws_sdk_appstream.types.filters

        out["Filters"] = aws_sdk_appstream.types.filters.serialize_aws_json_1_1(
            value["filters"]
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListExportImageTasksRequest:
    out: ListExportImageTasksRequest = {}  # type: ignore[typeddict-item]
    if "Filters" in data:
        import aws_sdk_appstream.types.filters

        out["filters"] = aws_sdk_appstream.types.filters.deserialize_aws_json_1_1(
            data["Filters"]
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
