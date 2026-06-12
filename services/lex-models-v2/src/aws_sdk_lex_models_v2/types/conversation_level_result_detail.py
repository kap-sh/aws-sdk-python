"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ConversationLevelResultDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.test_result_match_status


class ConversationLevelResultDetail(TypedDict):
    end_to_end_result: (
        "aws_sdk_lex_models_v2.types.test_result_match_status.TestResultMatchStatus"
    )
    """<p>The success or failure of the streaming of the conversation.</p>"""
    speech_transcription_result: NotRequired[
        "aws_sdk_lex_models_v2.types.test_result_match_status.TestResultMatchStatus"
    ]
    """<p>The speech transcription success or failure details of the conversation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConversationLevelResultDetail) -> dict:
    out: dict = {}
    import aws_sdk_lex_models_v2.types.test_result_match_status

    out["endToEndResult"] = (
        aws_sdk_lex_models_v2.types.test_result_match_status.serialize_json(
            value["end_to_end_result"]
        )
    )
    if "speech_transcription_result" in value:
        import aws_sdk_lex_models_v2.types.test_result_match_status

        out["speechTranscriptionResult"] = (
            aws_sdk_lex_models_v2.types.test_result_match_status.serialize_json(
                value["speech_transcription_result"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConversationLevelResultDetail:
    out: ConversationLevelResultDetail = {}  # type: ignore[typeddict-item]
    if "endToEndResult" in data:
        import aws_sdk_lex_models_v2.types.test_result_match_status

        out["end_to_end_result"] = (
            aws_sdk_lex_models_v2.types.test_result_match_status.deserialize_json(
                data["endToEndResult"]
            )
        )
    else:
        raise DeserializationError(
            "ConversationLevelResultDetail.end_to_end_result required"
        )
    if "speechTranscriptionResult" in data:
        import aws_sdk_lex_models_v2.types.test_result_match_status

        out["speech_transcription_result"] = (
            aws_sdk_lex_models_v2.types.test_result_match_status.deserialize_json(
                data["speechTranscriptionResult"]
            )
        )
    return out
