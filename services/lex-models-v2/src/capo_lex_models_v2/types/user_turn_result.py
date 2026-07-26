"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#UserTurnResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_models_v2.types.conversation_level_result_detail
    import capo_lex_models_v2.types.execution_error_details
    import capo_lex_models_v2.types.test_result_match_status
    import capo_lex_models_v2.types.user_turn_input_specification
    import capo_lex_models_v2.types.user_turn_output_specification


class UserTurnResult(TypedDict, closed=True):
    input: "capo_lex_models_v2.types.user_turn_input_specification.UserTurnInputSpecification"
    """<p>Contains information about the user messages in the turn in the input.</p>"""
    expected_output: "capo_lex_models_v2.types.user_turn_output_specification.UserTurnOutputSpecification"
    """<p>Contains information about the expected output for the user turn.</p>"""
    actual_output: NotRequired[
        "capo_lex_models_v2.types.user_turn_output_specification.UserTurnOutputSpecification"
    ]
    """<p>Contains information about the actual output for the user turn.</p>"""
    error_details: NotRequired[
        "capo_lex_models_v2.types.execution_error_details.ExecutionErrorDetails"
    ]
    end_to_end_result: NotRequired[
        "capo_lex_models_v2.types.test_result_match_status.TestResultMatchStatus"
    ]
    """<p>Specifies whether the expected and actual outputs match or not, or if there is an error in execution.</p>"""
    intent_match_result: NotRequired[
        "capo_lex_models_v2.types.test_result_match_status.TestResultMatchStatus"
    ]
    """<p>Specifies whether the expected and actual intents match or not.</p>"""
    slot_match_result: NotRequired[
        "capo_lex_models_v2.types.test_result_match_status.TestResultMatchStatus"
    ]
    """<p>Specifies whether the expected and actual slots match or not.</p>"""
    speech_transcription_result: NotRequired[
        "capo_lex_models_v2.types.test_result_match_status.TestResultMatchStatus"
    ]
    """<p>Specifies whether the expected and actual speech transcriptions match or not, or if there is an error in execution.</p>"""
    conversation_level_result: NotRequired[
        "capo_lex_models_v2.types.conversation_level_result_detail.ConversationLevelResultDetail"
    ]
    """<p>Contains information about the results related to the conversation associated with the user turn.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserTurnResult) -> dict:
    out: dict = {}
    import capo_lex_models_v2.types.user_turn_input_specification

    out["input"] = (
        capo_lex_models_v2.types.user_turn_input_specification.serialize_json(
            value["input"]
        )
    )
    import capo_lex_models_v2.types.user_turn_output_specification

    out["expectedOutput"] = (
        capo_lex_models_v2.types.user_turn_output_specification.serialize_json(
            value["expected_output"]
        )
    )
    if "actual_output" in value:
        import capo_lex_models_v2.types.user_turn_output_specification

        out["actualOutput"] = (
            capo_lex_models_v2.types.user_turn_output_specification.serialize_json(
                value["actual_output"]
            )
        )
    if "error_details" in value:
        import capo_lex_models_v2.types.execution_error_details

        out["errorDetails"] = (
            capo_lex_models_v2.types.execution_error_details.serialize_json(
                value["error_details"]
            )
        )
    if "end_to_end_result" in value:
        import capo_lex_models_v2.types.test_result_match_status

        out["endToEndResult"] = (
            capo_lex_models_v2.types.test_result_match_status.serialize_json(
                value["end_to_end_result"]
            )
        )
    if "intent_match_result" in value:
        import capo_lex_models_v2.types.test_result_match_status

        out["intentMatchResult"] = (
            capo_lex_models_v2.types.test_result_match_status.serialize_json(
                value["intent_match_result"]
            )
        )
    if "slot_match_result" in value:
        import capo_lex_models_v2.types.test_result_match_status

        out["slotMatchResult"] = (
            capo_lex_models_v2.types.test_result_match_status.serialize_json(
                value["slot_match_result"]
            )
        )
    if "speech_transcription_result" in value:
        import capo_lex_models_v2.types.test_result_match_status

        out["speechTranscriptionResult"] = (
            capo_lex_models_v2.types.test_result_match_status.serialize_json(
                value["speech_transcription_result"]
            )
        )
    if "conversation_level_result" in value:
        import capo_lex_models_v2.types.conversation_level_result_detail

        out["conversationLevelResult"] = (
            capo_lex_models_v2.types.conversation_level_result_detail.serialize_json(
                value["conversation_level_result"]
            )
        )
    return out


def deserialize_json(data: dict) -> UserTurnResult:
    out: UserTurnResult = {}  # type: ignore[typeddict-item]
    if "input" in data:
        import capo_lex_models_v2.types.user_turn_input_specification

        out["input"] = (
            capo_lex_models_v2.types.user_turn_input_specification.deserialize_json(
                data["input"]
            )
        )
    else:
        raise DeserializationError("UserTurnResult.input required")
    if "expectedOutput" in data:
        import capo_lex_models_v2.types.user_turn_output_specification

        out["expected_output"] = (
            capo_lex_models_v2.types.user_turn_output_specification.deserialize_json(
                data["expectedOutput"]
            )
        )
    else:
        raise DeserializationError("UserTurnResult.expected_output required")
    if "actualOutput" in data:
        import capo_lex_models_v2.types.user_turn_output_specification

        out["actual_output"] = (
            capo_lex_models_v2.types.user_turn_output_specification.deserialize_json(
                data["actualOutput"]
            )
        )
    if "errorDetails" in data:
        import capo_lex_models_v2.types.execution_error_details

        out["error_details"] = (
            capo_lex_models_v2.types.execution_error_details.deserialize_json(
                data["errorDetails"]
            )
        )
    if "endToEndResult" in data:
        import capo_lex_models_v2.types.test_result_match_status

        out["end_to_end_result"] = (
            capo_lex_models_v2.types.test_result_match_status.deserialize_json(
                data["endToEndResult"]
            )
        )
    if "intentMatchResult" in data:
        import capo_lex_models_v2.types.test_result_match_status

        out["intent_match_result"] = (
            capo_lex_models_v2.types.test_result_match_status.deserialize_json(
                data["intentMatchResult"]
            )
        )
    if "slotMatchResult" in data:
        import capo_lex_models_v2.types.test_result_match_status

        out["slot_match_result"] = (
            capo_lex_models_v2.types.test_result_match_status.deserialize_json(
                data["slotMatchResult"]
            )
        )
    if "speechTranscriptionResult" in data:
        import capo_lex_models_v2.types.test_result_match_status

        out["speech_transcription_result"] = (
            capo_lex_models_v2.types.test_result_match_status.deserialize_json(
                data["speechTranscriptionResult"]
            )
        )
    if "conversationLevelResult" in data:
        import capo_lex_models_v2.types.conversation_level_result_detail

        out["conversation_level_result"] = (
            capo_lex_models_v2.types.conversation_level_result_detail.deserialize_json(
                data["conversationLevelResult"]
            )
        )
    return out
