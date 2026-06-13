"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyAnnotatedChunk``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_annotated_content_list


class AutomatedReasoningPolicyAnnotatedChunk(TypedDict):
    page_number: NotRequired["int"]
    """<p>The page number where this chunk begins, if the document is divided into pages.</p>"""
    content: "aws_sdk_bedrock.types.automated_reasoning_policy_annotated_content_list.AutomatedReasoningPolicyAnnotatedContentList"
    """<p>The lines of text contained within this chunk, each annotated with its line number.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyAnnotatedChunk) -> dict:
    out: dict = {}
    if "page_number" in value:
        out["pageNumber"] = value["page_number"]
    import aws_sdk_bedrock.types.automated_reasoning_policy_annotated_content_list

    out["content"] = (
        aws_sdk_bedrock.types.automated_reasoning_policy_annotated_content_list.serialize_json(
            value["content"]
        )
    )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyAnnotatedChunk:
    out: AutomatedReasoningPolicyAnnotatedChunk = {}  # type: ignore[typeddict-item]
    if "pageNumber" in data:
        out["page_number"] = data["pageNumber"]
    if "content" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_annotated_content_list

        out["content"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_annotated_content_list.deserialize_json(
                data["content"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyAnnotatedChunk.content required"
        )
    return out
