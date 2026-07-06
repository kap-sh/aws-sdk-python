"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#IntentClassificationTestResultItemCounts``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.count
    import aws_sdk_lex_models_v2.types.test_result_match_status_count_map


class IntentClassificationTestResultItemCounts(TypedDict, closed=True):
    total_result_count: "aws_sdk_lex_models_v2.types.count.Count"
    """<p>The total number of results in the intent classification test.</p>"""
    speech_transcription_result_counts: NotRequired[
        "aws_sdk_lex_models_v2.types.test_result_match_status_count_map.TestResultMatchStatusCountMap"
    ]
    """<p>The number of matched, mismatched, and execution error results for speech transcription for the intent.</p>"""
    intent_match_result_counts: "aws_sdk_lex_models_v2.types.test_result_match_status_count_map.TestResultMatchStatusCountMap"
    """<p>The number of matched and mismatched results for intent recognition for the intent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntentClassificationTestResultItemCounts) -> dict:
    out: dict = {}
    out["totalResultCount"] = value["total_result_count"]
    if "speech_transcription_result_counts" in value:
        import aws_sdk_lex_models_v2.types.test_result_match_status_count_map

        out["speechTranscriptionResultCounts"] = (
            aws_sdk_lex_models_v2.types.test_result_match_status_count_map.serialize_json(
                value["speech_transcription_result_counts"]
            )
        )
    import aws_sdk_lex_models_v2.types.test_result_match_status_count_map

    out["intentMatchResultCounts"] = (
        aws_sdk_lex_models_v2.types.test_result_match_status_count_map.serialize_json(
            value["intent_match_result_counts"]
        )
    )
    return out


def deserialize_json(data: dict) -> IntentClassificationTestResultItemCounts:
    out: IntentClassificationTestResultItemCounts = {}  # type: ignore[typeddict-item]
    if "totalResultCount" in data:
        out["total_result_count"] = data["totalResultCount"]
    else:
        raise DeserializationError(
            "IntentClassificationTestResultItemCounts.total_result_count required"
        )
    if "speechTranscriptionResultCounts" in data:
        import aws_sdk_lex_models_v2.types.test_result_match_status_count_map

        out["speech_transcription_result_counts"] = (
            aws_sdk_lex_models_v2.types.test_result_match_status_count_map.deserialize_json(
                data["speechTranscriptionResultCounts"]
            )
        )
    if "intentMatchResultCounts" in data:
        import aws_sdk_lex_models_v2.types.test_result_match_status_count_map

        out["intent_match_result_counts"] = (
            aws_sdk_lex_models_v2.types.test_result_match_status_count_map.deserialize_json(
                data["intentMatchResultCounts"]
            )
        )
    else:
        raise DeserializationError(
            "IntentClassificationTestResultItemCounts.intent_match_result_counts required"
        )
    return out
