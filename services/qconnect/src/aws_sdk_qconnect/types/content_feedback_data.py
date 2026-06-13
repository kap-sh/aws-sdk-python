"""Generated from Smithy shape ``com.amazonaws.qconnect#ContentFeedbackData``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_qconnect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.generative_content_feedback_data


class _ContentFeedbackData_generativeContentFeedbackData(TypedDict):
    generativeContentFeedbackData: "aws_sdk_qconnect.types.generative_content_feedback_data.GenerativeContentFeedbackData"


ContentFeedbackData: TypeAlias = _ContentFeedbackData_generativeContentFeedbackData


# --- restJson1 ser/de ---
def serialize_json(value: ContentFeedbackData) -> dict:
    if "generativeContentFeedbackData" in value:
        import aws_sdk_qconnect.types.generative_content_feedback_data

        return {
            "generativeContentFeedbackData": aws_sdk_qconnect.types.generative_content_feedback_data.serialize_json(
                value["generativeContentFeedbackData"]
            )
        }
    else:
        raise SerializationError("ContentFeedbackData: no variant present")


def deserialize_json(data: dict) -> ContentFeedbackData:
    if "generativeContentFeedbackData" in data:
        import aws_sdk_qconnect.types.generative_content_feedback_data

        return {
            "generativeContentFeedbackData": aws_sdk_qconnect.types.generative_content_feedback_data.deserialize_json(
                data["generativeContentFeedbackData"]
            )
        }
    else:
        raise DeserializationError("ContentFeedbackData: no recognized variant key")
