"""Generated from Smithy shape ``com.amazonaws.cleanrooms#SchemaAnalysisRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.analysis_rule_type
    import capo_cleanrooms.types.table_alias


class SchemaAnalysisRuleRequest(TypedDict, closed=True):
    name: "capo_cleanrooms.types.table_alias.TableAlias"
    """<p>The name of the analysis rule schema that you are requesting.</p>"""
    type: "capo_cleanrooms.types.analysis_rule_type.AnalysisRuleType"
    """<p>The type of analysis rule schema that you are requesting.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SchemaAnalysisRuleRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_cleanrooms.types.analysis_rule_type

    out["type"] = capo_cleanrooms.types.analysis_rule_type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> SchemaAnalysisRuleRequest:
    out: SchemaAnalysisRuleRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("SchemaAnalysisRuleRequest.name required")
    if "type" in data:
        import capo_cleanrooms.types.analysis_rule_type

        out["type"] = capo_cleanrooms.types.analysis_rule_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("SchemaAnalysisRuleRequest.type required")
    return out
