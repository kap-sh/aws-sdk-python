"""Generated from Smithy shape ``com.amazonaws.sesv2#TopicFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.topic_name
    import aws_sdk_sesv2.types.use_default_if_preference_unavailable


class TopicFilter(TypedDict):
    topic_name: NotRequired["aws_sdk_sesv2.types.topic_name.TopicName"]
    """<p>The name of a topic on which you wish to apply the filter.</p>"""
    use_default_if_preference_unavailable: "aws_sdk_sesv2.types.use_default_if_preference_unavailable.UseDefaultIfPreferenceUnavailable"
    """<p>Notes that the default subscription status should be applied to a contact because the contact has not noted their preference for subscribing to a topic.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicFilter) -> dict:
    out: dict = {}
    if "topic_name" in value:
        out["TopicName"] = value["topic_name"]
    out["UseDefaultIfPreferenceUnavailable"] = value.get(
        "use_default_if_preference_unavailable", False
    )
    return out


def deserialize_json(data: dict) -> TopicFilter:
    out: TopicFilter = {}  # type: ignore[typeddict-item]
    if "TopicName" in data:
        out["topic_name"] = data["TopicName"]
    if "UseDefaultIfPreferenceUnavailable" in data:
        out["use_default_if_preference_unavailable"] = data[
            "UseDefaultIfPreferenceUnavailable"
        ]
    else:
        out["use_default_if_preference_unavailable"] = False
    return out
