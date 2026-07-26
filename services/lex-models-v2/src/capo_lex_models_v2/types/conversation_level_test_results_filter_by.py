"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ConversationLevelTestResultsFilterBy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.test_result_match_status


class ConversationLevelTestResultsFilterBy(TypedDict, closed=True):
    end_to_end_result: NotRequired[
        "capo_lex_models_v2.types.test_result_match_status.TestResultMatchStatus"
    ]
    """<p>The selection of matched or mismatched end-to-end status to filter test set results data at the conversation level.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConversationLevelTestResultsFilterBy) -> dict:
    out: dict = {}
    if "end_to_end_result" in value:
        import capo_lex_models_v2.types.test_result_match_status

        out["endToEndResult"] = (
            capo_lex_models_v2.types.test_result_match_status.serialize_json(
                value["end_to_end_result"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConversationLevelTestResultsFilterBy:
    out: ConversationLevelTestResultsFilterBy = {}  # type: ignore[typeddict-item]
    if "endToEndResult" in data:
        import capo_lex_models_v2.types.test_result_match_status

        out["end_to_end_result"] = (
            capo_lex_models_v2.types.test_result_match_status.deserialize_json(
                data["endToEndResult"]
            )
        )
    return out
