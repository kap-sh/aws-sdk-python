"""Generated from Smithy shape ``com.amazonaws.workdocs#CreateNotificationSubscriptionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_workdocs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.id_type
    import aws_sdk_workdocs.types.subscription_end_point_type
    import aws_sdk_workdocs.types.subscription_protocol_type
    import aws_sdk_workdocs.types.subscription_type


class CreateNotificationSubscriptionRequest(TypedDict, closed=True):
    organization_id: "aws_sdk_workdocs.types.id_type.IdType"
    """<p>The ID of the organization.</p>"""
    endpoint: (
        "aws_sdk_workdocs.types.subscription_end_point_type.SubscriptionEndPointType"
    )
    """<p>The endpoint to receive the notifications. If the protocol is HTTPS, the endpoint is a URL that begins with <code>https</code>.</p>"""
    protocol: (
        "aws_sdk_workdocs.types.subscription_protocol_type.SubscriptionProtocolType"
    )
    """<p>The protocol to use. The supported value is https, which delivers JSON-encoded messages using HTTPS POST.</p>"""
    subscription_type: "aws_sdk_workdocs.types.subscription_type.SubscriptionType"
    """<p>The notification type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateNotificationSubscriptionRequest) -> dict:
    out: dict = {}
    out["Endpoint"] = value["endpoint"]
    import aws_sdk_workdocs.types.subscription_protocol_type

    out["Protocol"] = aws_sdk_workdocs.types.subscription_protocol_type.serialize_json(
        value["protocol"]
    )
    import aws_sdk_workdocs.types.subscription_type

    out["SubscriptionType"] = aws_sdk_workdocs.types.subscription_type.serialize_json(
        value["subscription_type"]
    )
    return out


def deserialize_json(data: dict) -> CreateNotificationSubscriptionRequest:
    out: CreateNotificationSubscriptionRequest = {}  # type: ignore[typeddict-item]
    if "Endpoint" in data:
        out["endpoint"] = data["Endpoint"]
    else:
        raise DeserializationError(
            "CreateNotificationSubscriptionRequest.endpoint required"
        )
    if "Protocol" in data:
        import aws_sdk_workdocs.types.subscription_protocol_type

        out["protocol"] = (
            aws_sdk_workdocs.types.subscription_protocol_type.deserialize_json(
                data["Protocol"]
            )
        )
    else:
        raise DeserializationError(
            "CreateNotificationSubscriptionRequest.protocol required"
        )
    if "SubscriptionType" in data:
        import aws_sdk_workdocs.types.subscription_type

        out["subscription_type"] = (
            aws_sdk_workdocs.types.subscription_type.deserialize_json(
                data["SubscriptionType"]
            )
        )
    else:
        raise DeserializationError(
            "CreateNotificationSubscriptionRequest.subscription_type required"
        )
    return out
