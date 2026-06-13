"""Generated from Smithy shape ``com.amazonaws.securitylake#CreateSubscriberNotificationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securitylake.types.safe_string


class CreateSubscriberNotificationResponse(TypedDict):
    subscriber_endpoint: NotRequired[
        "aws_sdk_securitylake.types.safe_string.SafeString"
    ]
    """<p>The subscriber endpoint to which exception messages are posted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSubscriberNotificationResponse) -> dict:
    out: dict = {}
    if "subscriber_endpoint" in value:
        out["subscriberEndpoint"] = value["subscriber_endpoint"]
    return out


def deserialize_json(data: dict) -> CreateSubscriberNotificationResponse:
    out: CreateSubscriberNotificationResponse = {}  # type: ignore[typeddict-item]
    if "subscriberEndpoint" in data:
        out["subscriber_endpoint"] = data["subscriberEndpoint"]
    return out
