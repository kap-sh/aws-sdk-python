"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ConversationLevelTestResultItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.conversation_level_intent_classification_results
    import aws_sdk_lex_models_v2.types.conversation_level_slot_resolution_results
    import aws_sdk_lex_models_v2.types.test_result_match_status
    import aws_sdk_lex_models_v2.types.test_set_conversation_id


class ConversationLevelTestResultItem(TypedDict, closed=True):
    conversation_id: (
        "aws_sdk_lex_models_v2.types.test_set_conversation_id.TestSetConversationId"
    )
    """<p>The conversation Id of the test result evaluation item.</p>"""
    end_to_end_result: (
        "aws_sdk_lex_models_v2.types.test_result_match_status.TestResultMatchStatus"
    )
    """<p>The end-to-end success or failure of the test result evaluation item.</p>"""
    speech_transcription_result: NotRequired[
        "aws_sdk_lex_models_v2.types.test_result_match_status.TestResultMatchStatus"
    ]
    """<p>The speech transcription success or failure of the test result evaluation item.</p>"""
    intent_classification_results: "aws_sdk_lex_models_v2.types.conversation_level_intent_classification_results.ConversationLevelIntentClassificationResults"
    """<p>The intent classification of the test result evaluation item.</p>"""
    slot_resolution_results: "aws_sdk_lex_models_v2.types.conversation_level_slot_resolution_results.ConversationLevelSlotResolutionResults"
    """<p>The slot success or failure of the test result evaluation item.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConversationLevelTestResultItem) -> dict:
    out: dict = {}
    out["conversationId"] = value["conversation_id"]
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
    import aws_sdk_lex_models_v2.types.conversation_level_intent_classification_results

    out["intentClassificationResults"] = (
        aws_sdk_lex_models_v2.types.conversation_level_intent_classification_results.serialize_json(
            value["intent_classification_results"]
        )
    )
    import aws_sdk_lex_models_v2.types.conversation_level_slot_resolution_results

    out["slotResolutionResults"] = (
        aws_sdk_lex_models_v2.types.conversation_level_slot_resolution_results.serialize_json(
            value["slot_resolution_results"]
        )
    )
    return out


def deserialize_json(data: dict) -> ConversationLevelTestResultItem:
    out: ConversationLevelTestResultItem = {}  # type: ignore[typeddict-item]
    if "conversationId" in data:
        out["conversation_id"] = data["conversationId"]
    else:
        raise DeserializationError(
            "ConversationLevelTestResultItem.conversation_id required"
        )
    if "endToEndResult" in data:
        import aws_sdk_lex_models_v2.types.test_result_match_status

        out["end_to_end_result"] = (
            aws_sdk_lex_models_v2.types.test_result_match_status.deserialize_json(
                data["endToEndResult"]
            )
        )
    else:
        raise DeserializationError(
            "ConversationLevelTestResultItem.end_to_end_result required"
        )
    if "speechTranscriptionResult" in data:
        import aws_sdk_lex_models_v2.types.test_result_match_status

        out["speech_transcription_result"] = (
            aws_sdk_lex_models_v2.types.test_result_match_status.deserialize_json(
                data["speechTranscriptionResult"]
            )
        )
    if "intentClassificationResults" in data:
        import aws_sdk_lex_models_v2.types.conversation_level_intent_classification_results

        out["intent_classification_results"] = (
            aws_sdk_lex_models_v2.types.conversation_level_intent_classification_results.deserialize_json(
                data["intentClassificationResults"]
            )
        )
    else:
        raise DeserializationError(
            "ConversationLevelTestResultItem.intent_classification_results required"
        )
    if "slotResolutionResults" in data:
        import aws_sdk_lex_models_v2.types.conversation_level_slot_resolution_results

        out["slot_resolution_results"] = (
            aws_sdk_lex_models_v2.types.conversation_level_slot_resolution_results.deserialize_json(
                data["slotResolutionResults"]
            )
        )
    else:
        raise DeserializationError(
            "ConversationLevelTestResultItem.slot_resolution_results required"
        )
    return out
