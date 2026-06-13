"""Generated from Smithy shape ``com.amazonaws.securitylake#GetSubscriberRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securitylake.types.uuid


class GetSubscriberRequest(TypedDict):
    subscriber_id: "aws_sdk_securitylake.types.uuid.UUID"
    """<p>A value created by Amazon Security Lake that uniquely identifies your <code>GetSubscriber</code> API request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSubscriberRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSubscriberRequest:
    out: GetSubscriberRequest = {}  # type: ignore[typeddict-item]
    return out
