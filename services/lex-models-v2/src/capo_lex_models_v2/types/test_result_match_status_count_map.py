"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TestResultMatchStatusCountMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.count
    import capo_lex_models_v2.types.test_result_match_status

TestResultMatchStatusCountMap: TypeAlias = dict[
    "capo_lex_models_v2.types.test_result_match_status.TestResultMatchStatus",
    "capo_lex_models_v2.types.count.Count",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: TestResultMatchStatusCountMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_lex_models_v2.types.test_result_match_status

        out[capo_lex_models_v2.types.test_result_match_status.serialize_json(key)] = (
            value
        )
    return out


def deserialize_json(data: dict) -> TestResultMatchStatusCountMap:
    out: TestResultMatchStatusCountMap = {}
    for key, value in data.items():
        import capo_lex_models_v2.types.test_result_match_status

        out[capo_lex_models_v2.types.test_result_match_status.deserialize_json(key)] = (
            value
        )
    return out
