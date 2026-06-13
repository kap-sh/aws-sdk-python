"""Generated from Smithy shape ``com.amazonaws.securitylake#UpdateDataLakeExceptionSubscriptionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_securitylake.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_securitylake.types.safe_string
    import aws_sdk_securitylake.types.subscription_protocol


class UpdateDataLakeExceptionSubscriptionRequest(TypedDict):
    subscription_protocol: (
        "aws_sdk_securitylake.types.subscription_protocol.SubscriptionProtocol"
    )
    """<p>The subscription protocol to which exception messages are posted.</p>"""
    notification_endpoint: "aws_sdk_securitylake.types.safe_string.SafeString"
    """<p>The account that is subscribed to receive exception notifications.</p>"""
    exception_time_to_live: NotRequired["int"]
    """<p>The time-to-live (TTL) for the exception message to remain. It is the duration of time until which the exception message remains. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDataLakeExceptionSubscriptionRequest) -> dict:
    out: dict = {}
    out["subscriptionProtocol"] = value["subscription_protocol"]
    out["notificationEndpoint"] = value["notification_endpoint"]
    if "exception_time_to_live" in value:
        out["exceptionTimeToLive"] = value["exception_time_to_live"]
    return out


def deserialize_json(data: dict) -> UpdateDataLakeExceptionSubscriptionRequest:
    out: UpdateDataLakeExceptionSubscriptionRequest = {}  # type: ignore[typeddict-item]
    if "subscriptionProtocol" in data:
        out["subscription_protocol"] = data["subscriptionProtocol"]
    else:
        raise DeserializationError(
            "UpdateDataLakeExceptionSubscriptionRequest.subscription_protocol required"
        )
    if "notificationEndpoint" in data:
        out["notification_endpoint"] = data["notificationEndpoint"]
    else:
        raise DeserializationError(
            "UpdateDataLakeExceptionSubscriptionRequest.notification_endpoint required"
        )
    if "exceptionTimeToLive" in data:
        out["exception_time_to_live"] = data["exceptionTimeToLive"]
    return out
