"""Generated from Smithy shape ``com.amazonaws.inspector2#ProjectPeriodicScanConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.frequency_expression
    import aws_sdk_inspector2.types.rule_set_categories


class ProjectPeriodicScanConfiguration(TypedDict, closed=True):
    frequency_expression: NotRequired[
        "aws_sdk_inspector2.types.frequency_expression.FrequencyExpression"
    ]
    """<p>The schedule expression for periodic scans, in cron format, applied to the project.</p>"""
    rule_set_categories: NotRequired[
        "aws_sdk_inspector2.types.rule_set_categories.RuleSetCategories"
    ]
    """<p>The categories of security rules applied during periodic scans for the project.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProjectPeriodicScanConfiguration) -> dict:
    out: dict = {}
    if "frequency_expression" in value:
        out["frequencyExpression"] = value["frequency_expression"]
    if "rule_set_categories" in value:
        import aws_sdk_inspector2.types.rule_set_categories

        out["ruleSetCategories"] = (
            aws_sdk_inspector2.types.rule_set_categories.serialize_json(
                value["rule_set_categories"]
            )
        )
    return out


def deserialize_json(data: dict) -> ProjectPeriodicScanConfiguration:
    out: ProjectPeriodicScanConfiguration = {}  # type: ignore[typeddict-item]
    if "frequencyExpression" in data:
        out["frequency_expression"] = data["frequencyExpression"]
    if "ruleSetCategories" in data:
        import aws_sdk_inspector2.types.rule_set_categories

        out["rule_set_categories"] = (
            aws_sdk_inspector2.types.rule_set_categories.deserialize_json(
                data["ruleSetCategories"]
            )
        )
    return out
