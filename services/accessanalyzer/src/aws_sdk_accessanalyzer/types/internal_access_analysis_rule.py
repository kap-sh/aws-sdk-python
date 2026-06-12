"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#InternalAccessAnalysisRule``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.internal_access_analysis_rule_criteria_list


class InternalAccessAnalysisRule(TypedDict):
    inclusions: NotRequired[
        "aws_sdk_accessanalyzer.types.internal_access_analysis_rule_criteria_list.InternalAccessAnalysisRuleCriteriaList"
    ]
    """<p>A list of rules for the internal access analyzer containing criteria to include in analysis. Only resources that meet the rule criteria will generate findings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InternalAccessAnalysisRule) -> dict:
    out: dict = {}
    if "inclusions" in value:
        import aws_sdk_accessanalyzer.types.internal_access_analysis_rule_criteria_list

        out["inclusions"] = (
            aws_sdk_accessanalyzer.types.internal_access_analysis_rule_criteria_list.serialize_json(
                value["inclusions"]
            )
        )
    return out


def deserialize_json(data: dict) -> InternalAccessAnalysisRule:
    out: InternalAccessAnalysisRule = {}  # type: ignore[typeddict-item]
    if "inclusions" in data:
        import aws_sdk_accessanalyzer.types.internal_access_analysis_rule_criteria_list

        out["inclusions"] = (
            aws_sdk_accessanalyzer.types.internal_access_analysis_rule_criteria_list.deserialize_json(
                data["inclusions"]
            )
        )
    return out
