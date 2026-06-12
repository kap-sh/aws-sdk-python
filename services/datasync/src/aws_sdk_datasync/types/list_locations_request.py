"""Generated from Smithy shape ``com.amazonaws.datasync#ListLocationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datasync.types.location_filters
    import aws_sdk_datasync.types.max_results
    import aws_sdk_datasync.types.next_token


class ListLocationsRequest(TypedDict):
    max_results: NotRequired["aws_sdk_datasync.types.max_results.MaxResults"]
    """<p>The maximum number of locations to return.</p>"""
    next_token: NotRequired["aws_sdk_datasync.types.next_token.NextToken"]
    """<p>An opaque string that indicates the position at which to begin the next list of locations.</p>"""
    filters: NotRequired["aws_sdk_datasync.types.location_filters.LocationFilters"]
    """<p>You can use API filters to narrow down the list of resources returned by <code>ListLocations</code>. For example, to retrieve all tasks on a specific source location, you can use <code>ListLocations</code> with filter name <code>LocationType S3</code> and <code>Operator Equals</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListLocationsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "filters" in value:
        import aws_sdk_datasync.types.location_filters

        out["Filters"] = aws_sdk_datasync.types.location_filters.serialize_aws_json_1_1(
            value["filters"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListLocationsRequest:
    out: ListLocationsRequest = {}  # type: ignore[typeddict-item]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Filters" in data:
        import aws_sdk_datasync.types.location_filters

        out["filters"] = (
            aws_sdk_datasync.types.location_filters.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    return out
