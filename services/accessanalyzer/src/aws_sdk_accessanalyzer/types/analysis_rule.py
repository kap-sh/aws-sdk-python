"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#AnalysisRule``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.analysis_rule_criteria_list


class AnalysisRule(TypedDict):
    exclusions: NotRequired[
        "aws_sdk_accessanalyzer.types.analysis_rule_criteria_list.AnalysisRuleCriteriaList"
    ]
    """<p>A list of rules for the analyzer containing criteria to exclude from analysis. Entities that meet the rule criteria will not generate findings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisRule) -> dict:
    out: dict = {}
    if "exclusions" in value:
        import aws_sdk_accessanalyzer.types.analysis_rule_criteria_list

        out["exclusions"] = (
            aws_sdk_accessanalyzer.types.analysis_rule_criteria_list.serialize_json(
                value["exclusions"]
            )
        )
    return out


def deserialize_json(data: dict) -> AnalysisRule:
    out: AnalysisRule = {}  # type: ignore[typeddict-item]
    if "exclusions" in data:
        import aws_sdk_accessanalyzer.types.analysis_rule_criteria_list

        out["exclusions"] = (
            aws_sdk_accessanalyzer.types.analysis_rule_criteria_list.deserialize_json(
                data["exclusions"]
            )
        )
    return out
