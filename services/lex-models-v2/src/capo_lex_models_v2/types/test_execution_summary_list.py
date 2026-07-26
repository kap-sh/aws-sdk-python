"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TestExecutionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.test_execution_summary

TestExecutionSummaryList: TypeAlias = list[
    "capo_lex_models_v2.types.test_execution_summary.TestExecutionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: TestExecutionSummaryList) -> list:
    import capo_lex_models_v2.types.test_execution_summary

    out: list = []
    for item in value:
        out.append(capo_lex_models_v2.types.test_execution_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> TestExecutionSummaryList:
    import capo_lex_models_v2.types.test_execution_summary

    out: TestExecutionSummaryList = []
    for item in data:
        out.append(
            capo_lex_models_v2.types.test_execution_summary.deserialize_json(item)
        )
    return out
