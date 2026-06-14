"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#SnsTopicConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.sns_topic_policy


class SnsTopicConfiguration(TypedDict):
    topic_policy: NotRequired[
        "aws_sdk_accessanalyzer.types.sns_topic_policy.SnsTopicPolicy"
    ]
    r"""<p>The JSON policy text that defines who can access an Amazon SNS topic. For more information, see <a href=\"https://docs.aws.amazon.com/sns/latest/dg/sns-access-policy-use-cases.html\">Example cases for Amazon SNS access control</a> in the <i>Amazon SNS Developer Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SnsTopicConfiguration) -> dict:
    out: dict = {}
    if "topic_policy" in value:
        out["topicPolicy"] = value["topic_policy"]
    return out


def deserialize_json(data: dict) -> SnsTopicConfiguration:
    out: SnsTopicConfiguration = {}  # type: ignore[typeddict-item]
    if "topicPolicy" in data:
        out["topic_policy"] = data["topicPolicy"]
    return out
