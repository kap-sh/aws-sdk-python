"""Generated from Smithy shape ``com.amazonaws.securitylake#DeleteSubscriberNotificationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_securitylake.types.uuid


class DeleteSubscriberNotificationRequest(TypedDict, closed=True):
    subscriber_id: "aws_sdk_securitylake.types.uuid.UUID"
    """<p>The ID of the Security Lake subscriber account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSubscriberNotificationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteSubscriberNotificationRequest:
    out: DeleteSubscriberNotificationRequest = {}  # type: ignore[typeddict-item]
    return out
