"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TestExecutionResultItems``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.conversation_level_test_results
    import aws_sdk_lex_models_v2.types.intent_classification_test_results
    import aws_sdk_lex_models_v2.types.intent_level_slot_resolution_test_results
    import aws_sdk_lex_models_v2.types.overall_test_results
    import aws_sdk_lex_models_v2.types.utterance_level_test_results


class TestExecutionResultItems(TypedDict):
    overall_test_results: NotRequired[
        "aws_sdk_lex_models_v2.types.overall_test_results.OverallTestResults"
    ]
    """<p>Overall results for the test execution, including the breakdown of conversations and single-input utterances.</p>"""
    conversation_level_test_results: NotRequired[
        "aws_sdk_lex_models_v2.types.conversation_level_test_results.ConversationLevelTestResults"
    ]
    """<p>Results related to conversations in the test set, including metrics about success and failure of conversations and intent and slot failures.</p>"""
    intent_classification_test_results: NotRequired[
        "aws_sdk_lex_models_v2.types.intent_classification_test_results.IntentClassificationTestResults"
    ]
    """<p>Intent recognition results aggregated by intent name. The aggregated results contain success and failure rates of intent recognition, speech transcriptions, and end-to-end conversations.</p>"""
    intent_level_slot_resolution_test_results: NotRequired[
        "aws_sdk_lex_models_v2.types.intent_level_slot_resolution_test_results.IntentLevelSlotResolutionTestResults"
    ]
    """<p>Slot resolution results aggregated by intent and slot name. The aggregated results contain success and failure rates of slot resolution, speech transcriptions, and end-to-end conversations</p>"""
    utterance_level_test_results: NotRequired[
        "aws_sdk_lex_models_v2.types.utterance_level_test_results.UtteranceLevelTestResults"
    ]
    """<p>Results related to utterances in the test set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestExecutionResultItems) -> dict:
    out: dict = {}
    if "overall_test_results" in value:
        import aws_sdk_lex_models_v2.types.overall_test_results

        out["overallTestResults"] = (
            aws_sdk_lex_models_v2.types.overall_test_results.serialize_json(
                value["overall_test_results"]
            )
        )
    if "conversation_level_test_results" in value:
        import aws_sdk_lex_models_v2.types.conversation_level_test_results

        out["conversationLevelTestResults"] = (
            aws_sdk_lex_models_v2.types.conversation_level_test_results.serialize_json(
                value["conversation_level_test_results"]
            )
        )
    if "intent_classification_test_results" in value:
        import aws_sdk_lex_models_v2.types.intent_classification_test_results

        out["intentClassificationTestResults"] = (
            aws_sdk_lex_models_v2.types.intent_classification_test_results.serialize_json(
                value["intent_classification_test_results"]
            )
        )
    if "intent_level_slot_resolution_test_results" in value:
        import aws_sdk_lex_models_v2.types.intent_level_slot_resolution_test_results

        out["intentLevelSlotResolutionTestResults"] = (
            aws_sdk_lex_models_v2.types.intent_level_slot_resolution_test_results.serialize_json(
                value["intent_level_slot_resolution_test_results"]
            )
        )
    if "utterance_level_test_results" in value:
        import aws_sdk_lex_models_v2.types.utterance_level_test_results

        out["utteranceLevelTestResults"] = (
            aws_sdk_lex_models_v2.types.utterance_level_test_results.serialize_json(
                value["utterance_level_test_results"]
            )
        )
    return out


def deserialize_json(data: dict) -> TestExecutionResultItems:
    out: TestExecutionResultItems = {}  # type: ignore[typeddict-item]
    if "overallTestResults" in data:
        import aws_sdk_lex_models_v2.types.overall_test_results

        out["overall_test_results"] = (
            aws_sdk_lex_models_v2.types.overall_test_results.deserialize_json(
                data["overallTestResults"]
            )
        )
    if "conversationLevelTestResults" in data:
        import aws_sdk_lex_models_v2.types.conversation_level_test_results

        out["conversation_level_test_results"] = (
            aws_sdk_lex_models_v2.types.conversation_level_test_results.deserialize_json(
                data["conversationLevelTestResults"]
            )
        )
    if "intentClassificationTestResults" in data:
        import aws_sdk_lex_models_v2.types.intent_classification_test_results

        out["intent_classification_test_results"] = (
            aws_sdk_lex_models_v2.types.intent_classification_test_results.deserialize_json(
                data["intentClassificationTestResults"]
            )
        )
    if "intentLevelSlotResolutionTestResults" in data:
        import aws_sdk_lex_models_v2.types.intent_level_slot_resolution_test_results

        out["intent_level_slot_resolution_test_results"] = (
            aws_sdk_lex_models_v2.types.intent_level_slot_resolution_test_results.deserialize_json(
                data["intentLevelSlotResolutionTestResults"]
            )
        )
    if "utteranceLevelTestResults" in data:
        import aws_sdk_lex_models_v2.types.utterance_level_test_results

        out["utterance_level_test_results"] = (
            aws_sdk_lex_models_v2.types.utterance_level_test_results.deserialize_json(
                data["utteranceLevelTestResults"]
            )
        )
    return out
