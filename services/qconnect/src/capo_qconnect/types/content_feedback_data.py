"""Generated from Smithy shape ``com.amazonaws.qconnect#ContentFeedbackData``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_qconnect.types.generative_content_feedback_data


class _ContentFeedbackData_generativeContentFeedbackData(TypedDict, closed=True):
    generativeContentFeedbackData: "capo_qconnect.types.generative_content_feedback_data.GenerativeContentFeedbackData"


ContentFeedbackData: TypeAlias = _ContentFeedbackData_generativeContentFeedbackData


# --- restJson1 ser/de ---
def serialize_json(value: ContentFeedbackData) -> dict:
    if "generativeContentFeedbackData" in value:
        import capo_qconnect.types.generative_content_feedback_data

        return {
            "generativeContentFeedbackData": capo_qconnect.types.generative_content_feedback_data.serialize_json(
                value["generativeContentFeedbackData"]
            )
        }
    else:
        raise SerializationError("ContentFeedbackData: no variant present")


def deserialize_json(data: dict) -> ContentFeedbackData:
    if "generativeContentFeedbackData" in data:
        import capo_qconnect.types.generative_content_feedback_data

        return {
            "generativeContentFeedbackData": capo_qconnect.types.generative_content_feedback_data.deserialize_json(
                data["generativeContentFeedbackData"]
            )
        }
    else:
        raise DeserializationError("ContentFeedbackData: no recognized variant key")
