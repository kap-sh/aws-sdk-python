"""Generated from Smithy shape ``com.amazonaws.personalize#DescribeEventTrackerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.event_tracker


class DescribeEventTrackerResponse(TypedDict, closed=True):
    event_tracker: NotRequired["capo_personalize.types.event_tracker.EventTracker"]
    """<p>An object that describes the event tracker.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEventTrackerResponse) -> dict:
    out: dict = {}
    if "event_tracker" in value:
        import capo_personalize.types.event_tracker

        out["eventTracker"] = (
            capo_personalize.types.event_tracker.serialize_aws_json_1_1(
                value["event_tracker"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEventTrackerResponse:
    out: DescribeEventTrackerResponse = {}  # type: ignore[typeddict-item]
    if "eventTracker" in data:
        import capo_personalize.types.event_tracker

        out["event_tracker"] = (
            capo_personalize.types.event_tracker.deserialize_aws_json_1_1(
                data["eventTracker"]
            )
        )
    return out
