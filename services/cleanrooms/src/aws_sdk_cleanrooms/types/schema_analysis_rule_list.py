"""Generated from Smithy shape ``com.amazonaws.cleanrooms#SchemaAnalysisRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.analysis_rule

SchemaAnalysisRuleList: TypeAlias = list[
    "aws_sdk_cleanrooms.types.analysis_rule.AnalysisRule"
]


# --- restJson1 ser/de ---
def serialize_json(value: SchemaAnalysisRuleList) -> list:
    import aws_sdk_cleanrooms.types.analysis_rule

    out: list = []
    for item in value:
        out.append(aws_sdk_cleanrooms.types.analysis_rule.serialize_json(item))
    return out


def deserialize_json(data: list) -> SchemaAnalysisRuleList:
    import aws_sdk_cleanrooms.types.analysis_rule

    out: SchemaAnalysisRuleList = []
    for item in data:
        out.append(aws_sdk_cleanrooms.types.analysis_rule.deserialize_json(item))
    return out
