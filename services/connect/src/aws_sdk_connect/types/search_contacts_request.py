"""Generated from Smithy shape ``com.amazonaws.connect#SearchContactsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.large_next_token
    import aws_sdk_connect.types.max_result100
    import aws_sdk_connect.types.search_contacts_time_range
    import aws_sdk_connect.types.search_criteria
    import aws_sdk_connect.types.sort


class SearchContactsRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    """<p>The identifier of Connect Customer instance. You can find the instance ID in the Amazon Resource Name (ARN) of the instance.</p>"""
    time_range: (
        "aws_sdk_connect.types.search_contacts_time_range.SearchContactsTimeRange"
    )
    """<p>Time range that you want to search results.</p>"""
    search_criteria: NotRequired["aws_sdk_connect.types.search_criteria.SearchCriteria"]
    """<p>The search criteria to be used to return contacts.</p>"""
    max_results: NotRequired["aws_sdk_connect.types.max_result100.MaxResult100"]
    """<p>The maximum number of results to return per page.</p>"""
    next_token: NotRequired["aws_sdk_connect.types.large_next_token.LargeNextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    sort: NotRequired["aws_sdk_connect.types.sort.Sort"]
    """<p>Specifies a field to sort by and a sort order.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchContactsRequest) -> dict:
    out: dict = {}
    out["InstanceId"] = value["instance_id"]
    import aws_sdk_connect.types.search_contacts_time_range

    out["TimeRange"] = aws_sdk_connect.types.search_contacts_time_range.serialize_json(
        value["time_range"]
    )
    if "search_criteria" in value:
        import aws_sdk_connect.types.search_criteria

        out["SearchCriteria"] = aws_sdk_connect.types.search_criteria.serialize_json(
            value["search_criteria"]
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "sort" in value:
        import aws_sdk_connect.types.sort

        out["Sort"] = aws_sdk_connect.types.sort.serialize_json(value["sort"])
    return out


def deserialize_json(data: dict) -> SearchContactsRequest:
    out: SearchContactsRequest = {}  # type: ignore[typeddict-item]
    if "InstanceId" in data:
        out["instance_id"] = data["InstanceId"]
    else:
        raise DeserializationError("SearchContactsRequest.instance_id required")
    if "TimeRange" in data:
        import aws_sdk_connect.types.search_contacts_time_range

        out["time_range"] = (
            aws_sdk_connect.types.search_contacts_time_range.deserialize_json(
                data["TimeRange"]
            )
        )
    else:
        raise DeserializationError("SearchContactsRequest.time_range required")
    if "SearchCriteria" in data:
        import aws_sdk_connect.types.search_criteria

        out["search_criteria"] = aws_sdk_connect.types.search_criteria.deserialize_json(
            data["SearchCriteria"]
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Sort" in data:
        import aws_sdk_connect.types.sort

        out["sort"] = aws_sdk_connect.types.sort.deserialize_json(data["Sort"])
    return out
