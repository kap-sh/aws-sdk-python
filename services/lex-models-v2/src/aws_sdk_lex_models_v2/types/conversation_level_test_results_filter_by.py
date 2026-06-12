"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ConversationLevelTestResultsFilterBy``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.test_result_match_status


class ConversationLevelTestResultsFilterBy(TypedDict):
    end_to_end_result: NotRequired[
        "aws_sdk_lex_models_v2.types.test_result_match_status.TestResultMatchStatus"
    ]
    """<p>The selection of matched or mismatched end-to-end status to filter test set results data at the conversation level.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConversationLevelTestResultsFilterBy) -> dict:
    out: dict = {}
    if "end_to_end_result" in value:
        import aws_sdk_lex_models_v2.types.test_result_match_status

        out["endToEndResult"] = (
            aws_sdk_lex_models_v2.types.test_result_match_status.serialize_json(
                value["end_to_end_result"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConversationLevelTestResultsFilterBy:
    out: ConversationLevelTestResultsFilterBy = {}  # type: ignore[typeddict-item]
    if "endToEndResult" in data:
        import aws_sdk_lex_models_v2.types.test_result_match_status

        out["end_to_end_result"] = (
            aws_sdk_lex_models_v2.types.test_result_match_status.deserialize_json(
                data["endToEndResult"]
            )
        )
    return out
