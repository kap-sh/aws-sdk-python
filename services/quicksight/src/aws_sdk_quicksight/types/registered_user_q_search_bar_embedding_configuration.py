"""Generated from Smithy shape ``com.amazonaws.quicksight#RegisteredUserQSearchBarEmbeddingConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.restrictive_resource_id


class RegisteredUserQSearchBarEmbeddingConfiguration(TypedDict):
    initial_topic_id: NotRequired[
        "aws_sdk_quicksight.types.restrictive_resource_id.RestrictiveResourceId"
    ]
    """<p>The ID of the legacy Q topic that you want to use as the starting topic in the Q search bar. To locate the topic ID of the topic that you want to use, open the <a href=\"https://quicksight.aws.amazon.com/\">Quick Sight console</a>, navigate to the <b>Topics</b> pane, and choose thre topic that you want to use. The <code>TopicID</code> is located in the URL of the topic that opens. When you select an initial topic, you can specify whether or not readers are allowed to select other topics from the list of available topics.</p> <p>If you don't specify an initial topic or if you specify a new reader experience topic, a list of all shared legacy topics is shown in the Q bar. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisteredUserQSearchBarEmbeddingConfiguration) -> dict:
    out: dict = {}
    if "initial_topic_id" in value:
        out["InitialTopicId"] = value["initial_topic_id"]
    return out


def deserialize_json(data: dict) -> RegisteredUserQSearchBarEmbeddingConfiguration:
    out: RegisteredUserQSearchBarEmbeddingConfiguration = {}  # type: ignore[typeddict-item]
    if "InitialTopicId" in data:
        out["initial_topic_id"] = data["InitialTopicId"]
    return out
