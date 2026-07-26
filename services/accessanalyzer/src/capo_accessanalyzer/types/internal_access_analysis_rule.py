"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#InternalAccessAnalysisRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.internal_access_analysis_rule_criteria_list


class InternalAccessAnalysisRule(TypedDict, closed=True):
    inclusions: NotRequired[
        "capo_accessanalyzer.types.internal_access_analysis_rule_criteria_list.InternalAccessAnalysisRuleCriteriaList"
    ]
    """<p>A list of rules for the internal access analyzer containing criteria to include in analysis. Only resources that meet the rule criteria will generate findings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InternalAccessAnalysisRule) -> dict:
    out: dict = {}
    if "inclusions" in value:
        import capo_accessanalyzer.types.internal_access_analysis_rule_criteria_list

        out["inclusions"] = (
            capo_accessanalyzer.types.internal_access_analysis_rule_criteria_list.serialize_json(
                value["inclusions"]
            )
        )
    return out


def deserialize_json(data: dict) -> InternalAccessAnalysisRule:
    out: InternalAccessAnalysisRule = {}  # type: ignore[typeddict-item]
    if "inclusions" in data:
        import capo_accessanalyzer.types.internal_access_analysis_rule_criteria_list

        out["inclusions"] = (
            capo_accessanalyzer.types.internal_access_analysis_rule_criteria_list.deserialize_json(
                data["inclusions"]
            )
        )
    return out
