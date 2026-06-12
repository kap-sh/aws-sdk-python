"""Generated from Smithy shape ``com.amazonaws.gamelift#ListLocationsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.list_locations_limit
    import aws_sdk_gamelift.types.location_filter_list
    import aws_sdk_gamelift.types.non_zero_and_max_string


class ListLocationsInput(TypedDict):
    filters: NotRequired[
        "aws_sdk_gamelift.types.location_filter_list.LocationFilterList"
    ]
    """<p>Filters the list for <code>AWS</code> or <code>CUSTOM</code> locations. Use this parameter to narrow down results to only Amazon Web Services-managed locations (Amazon EC2 or container) or only your custom locations (such as an Amazon GameLift Servers Anywhere fleet).</p>"""
    limit: NotRequired["aws_sdk_gamelift.types.list_locations_limit.ListLocationsLimit"]
    """<p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>"""
    next_token: NotRequired[
        "aws_sdk_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListLocationsInput) -> dict:
    out: dict = {}
    if "filters" in value:
        import aws_sdk_gamelift.types.location_filter_list

        out["Filters"] = (
            aws_sdk_gamelift.types.location_filter_list.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListLocationsInput:
    out: ListLocationsInput = {}  # type: ignore[typeddict-item]
    if "Filters" in data:
        import aws_sdk_gamelift.types.location_filter_list

        out["filters"] = (
            aws_sdk_gamelift.types.location_filter_list.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if "Limit" in data:
        out["limit"] = data["Limit"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
