"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#InlineArchiveRule``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_accessanalyzer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_accessanalyzer.types.filter_criteria_map
    import capo_accessanalyzer.types.name


class InlineArchiveRule(TypedDict, closed=True):
    rule_name: "capo_accessanalyzer.types.name.Name"
    """<p>The name of the rule.</p>"""
    filter: "capo_accessanalyzer.types.filter_criteria_map.FilterCriteriaMap"
    """<p>The condition and values for a criterion.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InlineArchiveRule) -> dict:
    out: dict = {}
    out["ruleName"] = value["rule_name"]
    import capo_accessanalyzer.types.filter_criteria_map

    out["filter"] = capo_accessanalyzer.types.filter_criteria_map.serialize_json(
        value["filter"]
    )
    return out


def deserialize_json(data: dict) -> InlineArchiveRule:
    out: InlineArchiveRule = {}  # type: ignore[typeddict-item]
    if "ruleName" in data:
        out["rule_name"] = data["ruleName"]
    else:
        raise DeserializationError("InlineArchiveRule.rule_name required")
    if "filter" in data:
        import capo_accessanalyzer.types.filter_criteria_map

        out["filter"] = capo_accessanalyzer.types.filter_criteria_map.deserialize_json(
            data["filter"]
        )
    else:
        raise DeserializationError("InlineArchiveRule.filter required")
    return out
