"""Generated from Smithy shape ``com.amazonaws.qbusiness#AutoSubscriptionConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.auto_subscription_status
    import aws_sdk_qbusiness.types.subscription_type


class AutoSubscriptionConfiguration(TypedDict):
    auto_subscribe: (
        "aws_sdk_qbusiness.types.auto_subscription_status.AutoSubscriptionStatus"
    )
    """<p>Describes whether automatic subscriptions are enabled for an Amazon Q Business application using IAM identity federation for user management.</p>"""
    default_subscription_type: NotRequired[
        "aws_sdk_qbusiness.types.subscription_type.SubscriptionType"
    ]
    """<p>Describes the default subscription type assigned to an Amazon Q Business application using IAM identity federation for user management. If the value for <code>autoSubscribe</code> is set to <code>ENABLED</code> you must select a value for this field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutoSubscriptionConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_qbusiness.types.auto_subscription_status

    out["autoSubscribe"] = (
        aws_sdk_qbusiness.types.auto_subscription_status.serialize_json(
            value["auto_subscribe"]
        )
    )
    if "default_subscription_type" in value:
        import aws_sdk_qbusiness.types.subscription_type

        out["defaultSubscriptionType"] = (
            aws_sdk_qbusiness.types.subscription_type.serialize_json(
                value["default_subscription_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> AutoSubscriptionConfiguration:
    out: AutoSubscriptionConfiguration = {}  # type: ignore[typeddict-item]
    if "autoSubscribe" in data:
        import aws_sdk_qbusiness.types.auto_subscription_status

        out["auto_subscribe"] = (
            aws_sdk_qbusiness.types.auto_subscription_status.deserialize_json(
                data["autoSubscribe"]
            )
        )
    else:
        raise DeserializationError(
            "AutoSubscriptionConfiguration.auto_subscribe required"
        )
    if "defaultSubscriptionType" in data:
        import aws_sdk_qbusiness.types.subscription_type

        out["default_subscription_type"] = (
            aws_sdk_qbusiness.types.subscription_type.deserialize_json(
                data["defaultSubscriptionType"]
            )
        )
    return out
