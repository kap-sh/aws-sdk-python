"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SlotResolutionTestResultItemCounts``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.count
    import aws_sdk_lex_models_v2.types.test_result_match_status_count_map


class SlotResolutionTestResultItemCounts(TypedDict, closed=True):
    total_result_count: "aws_sdk_lex_models_v2.types.count.Count"
    """<p>The total number of results.</p>"""
    speech_transcription_result_counts: NotRequired[
        "aws_sdk_lex_models_v2.types.test_result_match_status_count_map.TestResultMatchStatusCountMap"
    ]
    """<p>The number of matched, mismatched and execution error results for speech transcription for the slot.</p>"""
    slot_match_result_counts: "aws_sdk_lex_models_v2.types.test_result_match_status_count_map.TestResultMatchStatusCountMap"
    """<p>The number of matched and mismatched results for slot resolution for the slot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SlotResolutionTestResultItemCounts) -> dict:
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

    out["slotMatchResultCounts"] = (
        aws_sdk_lex_models_v2.types.test_result_match_status_count_map.serialize_json(
            value["slot_match_result_counts"]
        )
    )
    return out


def deserialize_json(data: dict) -> SlotResolutionTestResultItemCounts:
    out: SlotResolutionTestResultItemCounts = {}  # type: ignore[typeddict-item]
    if "totalResultCount" in data:
        out["total_result_count"] = data["totalResultCount"]
    else:
        raise DeserializationError(
            "SlotResolutionTestResultItemCounts.total_result_count required"
        )
    if "speechTranscriptionResultCounts" in data:
        import aws_sdk_lex_models_v2.types.test_result_match_status_count_map

        out["speech_transcription_result_counts"] = (
            aws_sdk_lex_models_v2.types.test_result_match_status_count_map.deserialize_json(
                data["speechTranscriptionResultCounts"]
            )
        )
    if "slotMatchResultCounts" in data:
        import aws_sdk_lex_models_v2.types.test_result_match_status_count_map

        out["slot_match_result_counts"] = (
            aws_sdk_lex_models_v2.types.test_result_match_status_count_map.deserialize_json(
                data["slotMatchResultCounts"]
            )
        )
    else:
        raise DeserializationError(
            "SlotResolutionTestResultItemCounts.slot_match_result_counts required"
        )
    return out
