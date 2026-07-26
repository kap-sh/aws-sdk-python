"""Generated from Smithy shape ``com.amazonaws.cleanrooms#BatchGetSchemaAnalysisRuleErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.batch_get_schema_analysis_rule_error

BatchGetSchemaAnalysisRuleErrorList: TypeAlias = list[
    "capo_cleanrooms.types.batch_get_schema_analysis_rule_error.BatchGetSchemaAnalysisRuleError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetSchemaAnalysisRuleErrorList) -> list:
    import capo_cleanrooms.types.batch_get_schema_analysis_rule_error

    out: list = []
    for item in value:
        out.append(
            capo_cleanrooms.types.batch_get_schema_analysis_rule_error.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchGetSchemaAnalysisRuleErrorList:
    import capo_cleanrooms.types.batch_get_schema_analysis_rule_error

    out: BatchGetSchemaAnalysisRuleErrorList = []
    for item in data:
        out.append(
            capo_cleanrooms.types.batch_get_schema_analysis_rule_error.deserialize_json(
                item
            )
        )
    return out
