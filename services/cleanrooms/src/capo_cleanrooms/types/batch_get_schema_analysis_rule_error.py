"""Generated from Smithy shape ``com.amazonaws.cleanrooms#BatchGetSchemaAnalysisRuleError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.analysis_rule_type
    import capo_cleanrooms.types.table_alias


class BatchGetSchemaAnalysisRuleError(TypedDict, closed=True):
    name: "capo_cleanrooms.types.table_alias.TableAlias"
    """<p>An error name for the error.</p>"""
    type: "capo_cleanrooms.types.analysis_rule_type.AnalysisRuleType"
    """<p>The analysis rule type.</p>"""
    code: "str"
    """<p>An error code for the error.</p>"""
    message: "str"
    """<p>A description of why the call failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetSchemaAnalysisRuleError) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_cleanrooms.types.analysis_rule_type

    out["type"] = capo_cleanrooms.types.analysis_rule_type.serialize_json(value["type"])
    out["code"] = value["code"]
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BatchGetSchemaAnalysisRuleError:
    out: BatchGetSchemaAnalysisRuleError = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("BatchGetSchemaAnalysisRuleError.name required")
    if "type" in data:
        import capo_cleanrooms.types.analysis_rule_type

        out["type"] = capo_cleanrooms.types.analysis_rule_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("BatchGetSchemaAnalysisRuleError.type required")
    if "code" in data:
        out["code"] = data["code"]
    else:
        raise DeserializationError("BatchGetSchemaAnalysisRuleError.code required")
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("BatchGetSchemaAnalysisRuleError.message required")
    return out
