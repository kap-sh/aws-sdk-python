"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeFleetEventsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.event_list
    import aws_sdk_gamelift.types.non_zero_and_max_string


class DescribeFleetEventsOutput(TypedDict, closed=True):
    events: NotRequired["aws_sdk_gamelift.types.event_list.EventList"]
    """<p>A collection of objects containing event log entries for the specified fleet.</p>"""
    next_token: NotRequired[
        "aws_sdk_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFleetEventsOutput) -> dict:
    out: dict = {}
    if "events" in value:
        import aws_sdk_gamelift.types.event_list

        out["Events"] = aws_sdk_gamelift.types.event_list.serialize_aws_json_1_1(
            value["events"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFleetEventsOutput:
    out: DescribeFleetEventsOutput = {}  # type: ignore[typeddict-item]
    if "Events" in data:
        import aws_sdk_gamelift.types.event_list

        out["events"] = aws_sdk_gamelift.types.event_list.deserialize_aws_json_1_1(
            data["Events"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
