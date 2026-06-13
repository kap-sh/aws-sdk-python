"""Generated from Smithy shape ``com.amazonaws.cleanrooms#SchemaAnalysisRuleRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.schema_analysis_rule_request

SchemaAnalysisRuleRequestList: TypeAlias = list[
    "aws_sdk_cleanrooms.types.schema_analysis_rule_request.SchemaAnalysisRuleRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: SchemaAnalysisRuleRequestList) -> list:
    import aws_sdk_cleanrooms.types.schema_analysis_rule_request

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cleanrooms.types.schema_analysis_rule_request.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SchemaAnalysisRuleRequestList:
    import aws_sdk_cleanrooms.types.schema_analysis_rule_request

    out: SchemaAnalysisRuleRequestList = []
    for item in data:
        out.append(
            aws_sdk_cleanrooms.types.schema_analysis_rule_request.deserialize_json(item)
        )
    return out
