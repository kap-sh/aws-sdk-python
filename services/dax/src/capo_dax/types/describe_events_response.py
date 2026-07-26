"""Generated from Smithy shape ``com.amazonaws.dax#DescribeEventsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dax.types.event_list
    import capo_dax.types.string


class DescribeEventsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_dax.types.string.String"]
    """<p>Provides an identifier to allow retrieval of paginated results.</p>"""
    events: NotRequired["capo_dax.types.event_list.EventList"]
    """<p>An array of events. Each element in the array represents one event.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEventsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "events" in value:
        import capo_dax.types.event_list

        out["Events"] = capo_dax.types.event_list.serialize_aws_json_1_1(
            value["events"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEventsResponse:
    out: DescribeEventsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Events" in data:
        import capo_dax.types.event_list

        out["events"] = capo_dax.types.event_list.deserialize_aws_json_1_1(
            data["Events"]
        )
    return out
