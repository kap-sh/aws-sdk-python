"""Generated from Smithy shape ``com.amazonaws.cognitosync#GetCognitoEventsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cognito_sync.types.events


class GetCognitoEventsResponse(TypedDict, closed=True):
    events: NotRequired["aws_sdk_cognito_sync.types.events.Events"]
    """<p>The Cognito Events returned from the GetCognitoEvents request</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCognitoEventsResponse) -> dict:
    out: dict = {}
    if "events" in value:
        import aws_sdk_cognito_sync.types.events

        out["Events"] = aws_sdk_cognito_sync.types.events.serialize_json(
            value["events"]
        )
    return out


def deserialize_json(data: dict) -> GetCognitoEventsResponse:
    out: GetCognitoEventsResponse = {}  # type: ignore[typeddict-item]
    if "Events" in data:
        import aws_sdk_cognito_sync.types.events

        out["events"] = aws_sdk_cognito_sync.types.events.deserialize_json(
            data["Events"]
        )
    return out
