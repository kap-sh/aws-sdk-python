"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#OverallTestResultItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.boolean
    import aws_sdk_lex_models_v2.types.count
    import aws_sdk_lex_models_v2.types.test_result_match_status_count_map


class OverallTestResultItem(TypedDict):
    multi_turn_conversation: "aws_sdk_lex_models_v2.types.boolean.Boolean"
    """<p>Indicates whether the conversation contains multiple turns or not.</p>"""
    total_result_count: "aws_sdk_lex_models_v2.types.count.Count"
    """<p>The total number of overall results in the result of the test execution.</p>"""
    speech_transcription_result_counts: NotRequired[
        "aws_sdk_lex_models_v2.types.test_result_match_status_count_map.TestResultMatchStatusCountMap"
    ]
    """<p>The number of speech transcription results in the overall test.</p>"""
    end_to_end_result_counts: "aws_sdk_lex_models_v2.types.test_result_match_status_count_map.TestResultMatchStatusCountMap"
    """<p>The number of results that succeeded.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OverallTestResultItem) -> dict:
    out: dict = {}
    out["multiTurnConversation"] = value.get("multi_turn_conversation", False)
    out["totalResultCount"] = value["total_result_count"]
    if "speech_transcription_result_counts" in value:
        import aws_sdk_lex_models_v2.types.test_result_match_status_count_map

        out["speechTranscriptionResultCounts"] = (
            aws_sdk_lex_models_v2.types.test_result_match_status_count_map.serialize_json(
                value["speech_transcription_result_counts"]
            )
        )
    import aws_sdk_lex_models_v2.types.test_result_match_status_count_map

    out["endToEndResultCounts"] = (
        aws_sdk_lex_models_v2.types.test_result_match_status_count_map.serialize_json(
            value["end_to_end_result_counts"]
        )
    )
    return out


def deserialize_json(data: dict) -> OverallTestResultItem:
    out: OverallTestResultItem = {}  # type: ignore[typeddict-item]
    if "multiTurnConversation" in data:
        out["multi_turn_conversation"] = data["multiTurnConversation"]
    else:
        out["multi_turn_conversation"] = False
    if "totalResultCount" in data:
        out["total_result_count"] = data["totalResultCount"]
    else:
        raise DeserializationError("OverallTestResultItem.total_result_count required")
    if "speechTranscriptionResultCounts" in data:
        import aws_sdk_lex_models_v2.types.test_result_match_status_count_map

        out["speech_transcription_result_counts"] = (
            aws_sdk_lex_models_v2.types.test_result_match_status_count_map.deserialize_json(
                data["speechTranscriptionResultCounts"]
            )
        )
    if "endToEndResultCounts" in data:
        import aws_sdk_lex_models_v2.types.test_result_match_status_count_map

        out["end_to_end_result_counts"] = (
            aws_sdk_lex_models_v2.types.test_result_match_status_count_map.deserialize_json(
                data["endToEndResultCounts"]
            )
        )
    else:
        raise DeserializationError(
            "OverallTestResultItem.end_to_end_result_counts required"
        )
    return out
