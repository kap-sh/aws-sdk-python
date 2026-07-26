"""Generated from Smithy shape ``com.amazonaws.connect#AttributeCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.comparison_operator
    import capo_connect.types.match_criteria
    import capo_connect.types.nullable_proficiency_level
    import capo_connect.types.predefined_attribute_name
    import capo_connect.types.proficiency_value
    import capo_connect.types.range


class AttributeCondition(TypedDict, closed=True):
    name: NotRequired[
        "capo_connect.types.predefined_attribute_name.PredefinedAttributeName"
    ]
    """<p>The name of predefined attribute.</p>"""
    value: NotRequired["capo_connect.types.proficiency_value.ProficiencyValue"]
    """<p>The value of predefined attribute.</p>"""
    proficiency_level: NotRequired[
        "capo_connect.types.nullable_proficiency_level.NullableProficiencyLevel"
    ]
    """<p>The proficiency level of the condition.</p>"""
    range: NotRequired["capo_connect.types.range.Range"]
    """<p>An Object to define the minimum and maximum proficiency levels.</p>"""
    match_criteria: NotRequired["capo_connect.types.match_criteria.MatchCriteria"]
    """<p>An object to define <code>AgentsCriteria</code>.</p>"""
    comparison_operator: NotRequired[
        "capo_connect.types.comparison_operator.ComparisonOperator"
    ]
    """<p>The operator of the condition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttributeCondition) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "value" in value:
        out["Value"] = value["value"]
    if "proficiency_level" in value:
        out["ProficiencyLevel"] = value["proficiency_level"]
    if "range" in value:
        import capo_connect.types.range

        out["Range"] = capo_connect.types.range.serialize_json(value["range"])
    if "match_criteria" in value:
        import capo_connect.types.match_criteria

        out["MatchCriteria"] = capo_connect.types.match_criteria.serialize_json(
            value["match_criteria"]
        )
    if "comparison_operator" in value:
        out["ComparisonOperator"] = value["comparison_operator"]
    return out


def deserialize_json(data: dict) -> AttributeCondition:
    out: AttributeCondition = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Value" in data:
        out["value"] = data["Value"]
    if "ProficiencyLevel" in data:
        out["proficiency_level"] = data["ProficiencyLevel"]
    if "Range" in data:
        import capo_connect.types.range

        out["range"] = capo_connect.types.range.deserialize_json(data["Range"])
    if "MatchCriteria" in data:
        import capo_connect.types.match_criteria

        out["match_criteria"] = capo_connect.types.match_criteria.deserialize_json(
            data["MatchCriteria"]
        )
    if "ComparisonOperator" in data:
        out["comparison_operator"] = data["ComparisonOperator"]
    return out
