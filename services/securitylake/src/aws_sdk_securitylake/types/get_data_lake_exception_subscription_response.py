"""Generated from Smithy shape ``com.amazonaws.securitylake#GetDataLakeExceptionSubscriptionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securitylake.types.safe_string
    import aws_sdk_securitylake.types.subscription_protocol


class GetDataLakeExceptionSubscriptionResponse(TypedDict, closed=True):
    subscription_protocol: NotRequired[
        "aws_sdk_securitylake.types.subscription_protocol.SubscriptionProtocol"
    ]
    """<p>The subscription protocol to which exception notifications are posted.</p>"""
    notification_endpoint: NotRequired[
        "aws_sdk_securitylake.types.safe_string.SafeString"
    ]
    """<p>The Amazon Web Services account where you receive exception notifications.</p>"""
    exception_time_to_live: NotRequired["int"]
    """<p>The expiration period and time-to-live (TTL). It is the duration of time until which the exception message remains.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataLakeExceptionSubscriptionResponse) -> dict:
    out: dict = {}
    if "subscription_protocol" in value:
        out["subscriptionProtocol"] = value["subscription_protocol"]
    if "notification_endpoint" in value:
        out["notificationEndpoint"] = value["notification_endpoint"]
    if "exception_time_to_live" in value:
        out["exceptionTimeToLive"] = value["exception_time_to_live"]
    return out


def deserialize_json(data: dict) -> GetDataLakeExceptionSubscriptionResponse:
    out: GetDataLakeExceptionSubscriptionResponse = {}  # type: ignore[typeddict-item]
    if "subscriptionProtocol" in data:
        out["subscription_protocol"] = data["subscriptionProtocol"]
    if "notificationEndpoint" in data:
        out["notification_endpoint"] = data["notificationEndpoint"]
    if "exceptionTimeToLive" in data:
        out["exception_time_to_live"] = data["exceptionTimeToLive"]
    return out
