"""Generated from Smithy shape ``com.amazonaws.quicksight#RegisteredUserGenerativeQnAEmbeddingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.restrictive_resource_id


class RegisteredUserGenerativeQnAEmbeddingConfiguration(TypedDict, closed=True):
    initial_topic_id: NotRequired[
        "capo_quicksight.types.restrictive_resource_id.RestrictiveResourceId"
    ]
    """<p>The ID of the new Q reader experience topic that you want to make the starting topic in the Generative Q&A experience. You can find a topic ID by navigating to the Topics pane in the Quick application and opening a topic. The ID is in the URL for the topic that you open.</p> <p>If you don't specify an initial topic or you specify a legacy topic, a list of all shared new reader experience topics is shown in the Generative Q&A experience for your readers. When you select an initial new reader experience topic, you can specify whether or not readers are allowed to select other new reader experience topics from the available ones in the list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisteredUserGenerativeQnAEmbeddingConfiguration) -> dict:
    out: dict = {}
    if "initial_topic_id" in value:
        out["InitialTopicId"] = value["initial_topic_id"]
    return out


def deserialize_json(data: dict) -> RegisteredUserGenerativeQnAEmbeddingConfiguration:
    out: RegisteredUserGenerativeQnAEmbeddingConfiguration = {}  # type: ignore[typeddict-item]
    if "InitialTopicId" in data:
        out["initial_topic_id"] = data["InitialTopicId"]
    return out
