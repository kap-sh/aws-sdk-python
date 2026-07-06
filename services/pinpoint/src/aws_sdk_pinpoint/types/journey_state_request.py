"""Generated from Smithy shape ``com.amazonaws.pinpoint#JourneyStateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.state


class JourneyStateRequest(TypedDict, closed=True):
    state: NotRequired["aws_sdk_pinpoint.types.state.State"]
    """<p>The status of the journey. Currently, Supported values are ACTIVE, PAUSED, and CANCELLED</p> <p>If you cancel a journey, Amazon Pinpoint continues to perform activities that are currently in progress, until those activities are complete. Amazon Pinpoint also continues to collect and aggregate analytics data for those activities, until they are complete, and any activities that were complete when you cancelled the journey.</p> <p>After you cancel a journey, you can't add, change, or remove any activities from the journey. In addition, Amazon Pinpoint stops evaluating the journey and doesn't perform any activities that haven't started.</p> <p>When the journey is paused, Amazon Pinpoint continues to perform activities that are currently in progress, until those activities are complete. Endpoints will stop entering journeys when the journey is paused and will resume entering the journey after the journey is resumed. For wait activities, wait time is paused when the journey is paused. Currently, PAUSED only supports journeys with a segment refresh interval.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JourneyStateRequest) -> dict:
    out: dict = {}
    if "state" in value:
        import aws_sdk_pinpoint.types.state

        out["State"] = aws_sdk_pinpoint.types.state.serialize_json(value["state"])
    return out


def deserialize_json(data: dict) -> JourneyStateRequest:
    out: JourneyStateRequest = {}  # type: ignore[typeddict-item]
    if "State" in data:
        import aws_sdk_pinpoint.types.state

        out["state"] = aws_sdk_pinpoint.types.state.deserialize_json(data["State"])
    return out
