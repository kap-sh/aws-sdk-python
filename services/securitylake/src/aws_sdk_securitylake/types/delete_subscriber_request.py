"""Generated from Smithy shape ``com.amazonaws.securitylake#DeleteSubscriberRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securitylake.types.uuid


class DeleteSubscriberRequest(TypedDict):
    subscriber_id: "aws_sdk_securitylake.types.uuid.UUID"
    """<p>A value created by Security Lake that uniquely identifies your <code>DeleteSubscriber</code> API request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSubscriberRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteSubscriberRequest:
    out: DeleteSubscriberRequest = {}  # type: ignore[typeddict-item]
    return out
