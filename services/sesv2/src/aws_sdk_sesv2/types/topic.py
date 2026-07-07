"""Generated from Smithy shape ``com.amazonaws.sesv2#Topic``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.description
    import aws_sdk_sesv2.types.display_name
    import aws_sdk_sesv2.types.subscription_status
    import aws_sdk_sesv2.types.topic_name


class Topic(TypedDict, closed=True):
    topic_name: "aws_sdk_sesv2.types.topic_name.TopicName"
    """<p>The name of the topic.</p>"""
    display_name: "aws_sdk_sesv2.types.display_name.DisplayName"
    """<p>The name of the topic the contact will see.</p>"""
    description: NotRequired["aws_sdk_sesv2.types.description.Description"]
    """<p>A description of what the topic is about, which the contact will see.</p>"""
    default_subscription_status: (
        "aws_sdk_sesv2.types.subscription_status.SubscriptionStatus"
    )
    """<p>The default subscription status to be applied to a contact if the contact has not noted their preference for subscribing to a topic.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Topic) -> dict:
    out: dict = {}
    out["TopicName"] = value["topic_name"]
    out["DisplayName"] = value["display_name"]
    if "description" in value:
        out["Description"] = value["description"]
    import aws_sdk_sesv2.types.subscription_status

    out["DefaultSubscriptionStatus"] = (
        aws_sdk_sesv2.types.subscription_status.serialize_json(
            value["default_subscription_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> Topic:
    out: Topic = {}  # type: ignore[typeddict-item]
    if "TopicName" in data:
        out["topic_name"] = data["TopicName"]
    else:
        raise DeserializationError("Topic.topic_name required")
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    else:
        raise DeserializationError("Topic.display_name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "DefaultSubscriptionStatus" in data:
        import aws_sdk_sesv2.types.subscription_status

        out["default_subscription_status"] = (
            aws_sdk_sesv2.types.subscription_status.deserialize_json(
                data["DefaultSubscriptionStatus"]
            )
        )
    else:
        raise DeserializationError("Topic.default_subscription_status required")
    return out
