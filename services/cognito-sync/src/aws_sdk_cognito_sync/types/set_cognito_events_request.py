"""Generated from Smithy shape ``com.amazonaws.cognitosync#SetCognitoEventsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cognito_sync.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_sync.types.events
    import aws_sdk_cognito_sync.types.identity_pool_id


class SetCognitoEventsRequest(TypedDict, closed=True):
    identity_pool_id: "aws_sdk_cognito_sync.types.identity_pool_id.IdentityPoolId"
    """<p>The Cognito Identity Pool to use when configuring Cognito Events</p>"""
    events: "aws_sdk_cognito_sync.types.events.Events"
    """<p>The events to configure</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SetCognitoEventsRequest) -> dict:
    out: dict = {}
    import aws_sdk_cognito_sync.types.events

    out["Events"] = aws_sdk_cognito_sync.types.events.serialize_json(value["events"])
    return out


def deserialize_json(data: dict) -> SetCognitoEventsRequest:
    out: SetCognitoEventsRequest = {}  # type: ignore[typeddict-item]
    if "Events" in data:
        import aws_sdk_cognito_sync.types.events

        out["events"] = aws_sdk_cognito_sync.types.events.deserialize_json(
            data["Events"]
        )
    else:
        raise DeserializationError("SetCognitoEventsRequest.events required")
    return out
