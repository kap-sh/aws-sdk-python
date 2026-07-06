"""Generated from Smithy shape ``com.amazonaws.securitylake#CreateDataLakeExceptionSubscriptionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_securitylake.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_securitylake.types.safe_string
    import aws_sdk_securitylake.types.subscription_protocol


class CreateDataLakeExceptionSubscriptionRequest(TypedDict, closed=True):
    subscription_protocol: (
        "aws_sdk_securitylake.types.subscription_protocol.SubscriptionProtocol"
    )
    """<p>The subscription protocol to which exception notifications are posted.</p>"""
    notification_endpoint: "aws_sdk_securitylake.types.safe_string.SafeString"
    """<p>The Amazon Web Services account where you want to receive exception notifications.</p>"""
    exception_time_to_live: NotRequired["int"]
    """<p>The expiration period and time-to-live (TTL). It is the duration of time until which the exception message remains.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataLakeExceptionSubscriptionRequest) -> dict:
    out: dict = {}
    out["subscriptionProtocol"] = value["subscription_protocol"]
    out["notificationEndpoint"] = value["notification_endpoint"]
    if "exception_time_to_live" in value:
        out["exceptionTimeToLive"] = value["exception_time_to_live"]
    return out


def deserialize_json(data: dict) -> CreateDataLakeExceptionSubscriptionRequest:
    out: CreateDataLakeExceptionSubscriptionRequest = {}  # type: ignore[typeddict-item]
    if "subscriptionProtocol" in data:
        out["subscription_protocol"] = data["subscriptionProtocol"]
    else:
        raise DeserializationError(
            "CreateDataLakeExceptionSubscriptionRequest.subscription_protocol required"
        )
    if "notificationEndpoint" in data:
        out["notification_endpoint"] = data["notificationEndpoint"]
    else:
        raise DeserializationError(
            "CreateDataLakeExceptionSubscriptionRequest.notification_endpoint required"
        )
    if "exceptionTimeToLive" in data:
        out["exception_time_to_live"] = data["exceptionTimeToLive"]
    return out
