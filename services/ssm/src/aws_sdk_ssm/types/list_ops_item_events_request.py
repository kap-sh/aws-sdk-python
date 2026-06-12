"""Generated from Smithy shape ``com.amazonaws.ssm#ListOpsItemEventsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.ops_item_event_filters
    import aws_sdk_ssm.types.ops_item_event_max_results
    import aws_sdk_ssm.types.string


class ListOpsItemEventsRequest(TypedDict):
    filters: NotRequired["aws_sdk_ssm.types.ops_item_event_filters.OpsItemEventFilters"]
    """<p>One or more OpsItem filters. Use a filter to return a more specific list of results. </p>"""
    max_results: NotRequired[
        "aws_sdk_ssm.types.ops_item_event_max_results.OpsItemEventMaxResults"
    ]
    """<p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results. </p>"""
    next_token: NotRequired["aws_sdk_ssm.types.string.String"]
    """<p>A token to start the list. Use this token to get the next set of results. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOpsItemEventsRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import aws_sdk_ssm.types.ops_item_event_filters

        out["Filters"] = (
            aws_sdk_ssm.types.ops_item_event_filters.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListOpsItemEventsRequest:
    out: ListOpsItemEventsRequest = {}  # type: ignore[typeddict-item]
    if "Filters" in data:
        import aws_sdk_ssm.types.ops_item_event_filters

        out["filters"] = (
            aws_sdk_ssm.types.ops_item_event_filters.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
