"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#ListTargetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codestar_notifications.types.list_targets_filters
    import aws_sdk_codestar_notifications.types.max_results
    import aws_sdk_codestar_notifications.types.next_token


class ListTargetsRequest(TypedDict, closed=True):
    filters: NotRequired[
        "aws_sdk_codestar_notifications.types.list_targets_filters.ListTargetsFilters"
    ]
    """<p>The filters to use to return information by service or resource type. Valid filters include target type, target address, and target status.</p> <note> <p>A filter with the same name can appear more than once when used with OR statements. Filters with different names should be applied with AND statements.</p> </note>"""
    next_token: NotRequired["aws_sdk_codestar_notifications.types.next_token.NextToken"]
    """<p>An enumeration token that, when provided in a request, returns the next batch of the results.</p>"""
    max_results: NotRequired[
        "aws_sdk_codestar_notifications.types.max_results.MaxResults"
    ]
    """<p>A non-negative integer used to limit the number of returned results. The maximum number of results that can be returned is 100.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTargetsRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import aws_sdk_codestar_notifications.types.list_targets_filters

        out["Filters"] = (
            aws_sdk_codestar_notifications.types.list_targets_filters.serialize_json(
                value["filters"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListTargetsRequest:
    out: ListTargetsRequest = {}  # type: ignore[typeddict-item]
    if "Filters" in data:
        import aws_sdk_codestar_notifications.types.list_targets_filters

        out["filters"] = (
            aws_sdk_codestar_notifications.types.list_targets_filters.deserialize_json(
                data["Filters"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
