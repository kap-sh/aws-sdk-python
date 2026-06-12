"""Generated from Smithy shape ``com.amazonaws.dax#DescribeEventsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dax.types.event_list
    import aws_sdk_dax.types.string


class DescribeEventsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_dax.types.string.String"]
    """<p>Provides an identifier to allow retrieval of paginated results.</p>"""
    events: NotRequired["aws_sdk_dax.types.event_list.EventList"]
    """<p>An array of events. Each element in the array represents one event.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEventsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "events" in value:
        import aws_sdk_dax.types.event_list

        out["Events"] = aws_sdk_dax.types.event_list.serialize_aws_json_1_1(
            value["events"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEventsResponse:
    out: DescribeEventsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Events" in data:
        import aws_sdk_dax.types.event_list

        out["events"] = aws_sdk_dax.types.event_list.deserialize_aws_json_1_1(
            data["Events"]
        )
    return out
