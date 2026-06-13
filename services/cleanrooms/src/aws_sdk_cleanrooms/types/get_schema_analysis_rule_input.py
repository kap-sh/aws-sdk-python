"""Generated from Smithy shape ``com.amazonaws.cleanrooms#GetSchemaAnalysisRuleInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.analysis_rule_type
    import aws_sdk_cleanrooms.types.collaboration_identifier
    import aws_sdk_cleanrooms.types.table_alias


class GetSchemaAnalysisRuleInput(TypedDict):
    collaboration_identifier: (
        "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier"
    )
    """<p>A unique identifier for the collaboration that the schema belongs to. Currently accepts a collaboration ID.</p>"""
    name: "aws_sdk_cleanrooms.types.table_alias.TableAlias"
    """<p>The name of the schema to retrieve the analysis rule for.</p>"""
    type: "aws_sdk_cleanrooms.types.analysis_rule_type.AnalysisRuleType"
    """<p>The type of the schema analysis rule to retrieve. Schema analysis rules are uniquely identified by a combination of the collaboration, the schema name, and their type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSchemaAnalysisRuleInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSchemaAnalysisRuleInput:
    out: GetSchemaAnalysisRuleInput = {}  # type: ignore[typeddict-item]
    return out
