"""Generated from Smithy shape ``com.amazonaws.sesv2#TopicPreference``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.subscription_status
    import aws_sdk_sesv2.types.topic_name


class TopicPreference(TypedDict):
    topic_name: "aws_sdk_sesv2.types.topic_name.TopicName"
    """<p>The name of the topic.</p>"""
    subscription_status: "aws_sdk_sesv2.types.subscription_status.SubscriptionStatus"
    """<p>The contact's subscription status to a topic which is either <code>OPT_IN</code> or <code>OPT_OUT</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicPreference) -> dict:
    out: dict = {}
    out["TopicName"] = value["topic_name"]
    import aws_sdk_sesv2.types.subscription_status

    out["SubscriptionStatus"] = aws_sdk_sesv2.types.subscription_status.serialize_json(
        value["subscription_status"]
    )
    return out


def deserialize_json(data: dict) -> TopicPreference:
    out: TopicPreference = {}  # type: ignore[typeddict-item]
    if "TopicName" in data:
        out["topic_name"] = data["TopicName"]
    else:
        raise DeserializationError("TopicPreference.topic_name required")
    if "SubscriptionStatus" in data:
        import aws_sdk_sesv2.types.subscription_status

        out["subscription_status"] = (
            aws_sdk_sesv2.types.subscription_status.deserialize_json(
                data["SubscriptionStatus"]
            )
        )
    else:
        raise DeserializationError("TopicPreference.subscription_status required")
    return out
