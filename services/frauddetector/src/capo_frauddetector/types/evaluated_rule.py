"""Generated from Smithy shape ``com.amazonaws.frauddetector#EvaluatedRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.boolean
    import capo_frauddetector.types.identifier
    import capo_frauddetector.types.list_of_strings
    import capo_frauddetector.types.sensitive_string
    import capo_frauddetector.types.whole_number_version_string


class EvaluatedRule(TypedDict, closed=True):
    rule_id: NotRequired["capo_frauddetector.types.identifier.identifier"]
    """<p> The rule ID. </p>"""
    rule_version: NotRequired[
        "capo_frauddetector.types.whole_number_version_string.wholeNumberVersionString"
    ]
    """<p> The rule version. </p>"""
    expression: NotRequired["capo_frauddetector.types.sensitive_string.sensitiveString"]
    """<p> The rule expression. </p>"""
    expression_with_values: NotRequired[
        "capo_frauddetector.types.sensitive_string.sensitiveString"
    ]
    """<p> The rule expression value. </p>"""
    outcomes: NotRequired["capo_frauddetector.types.list_of_strings.ListOfStrings"]
    """<p> The rule outcome. </p>"""
    evaluated: NotRequired["capo_frauddetector.types.boolean.Boolean"]
    """<p> Indicates whether the rule was evaluated. </p>"""
    matched: NotRequired["capo_frauddetector.types.boolean.Boolean"]
    """<p> Indicates whether the rule matched. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EvaluatedRule) -> dict:
    out: dict = {}
    if "rule_id" in value:
        out["ruleId"] = value["rule_id"]
    if "rule_version" in value:
        out["ruleVersion"] = value["rule_version"]
    if "expression" in value:
        out["expression"] = value["expression"]
    if "expression_with_values" in value:
        out["expressionWithValues"] = value["expression_with_values"]
    if "outcomes" in value:
        import capo_frauddetector.types.list_of_strings

        out["outcomes"] = (
            capo_frauddetector.types.list_of_strings.serialize_aws_json_1_1(
                value["outcomes"]
            )
        )
    if "evaluated" in value:
        out["evaluated"] = value["evaluated"]
    if "matched" in value:
        out["matched"] = value["matched"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EvaluatedRule:
    out: EvaluatedRule = {}  # type: ignore[typeddict-item]
    if "ruleId" in data:
        out["rule_id"] = data["ruleId"]
    if "ruleVersion" in data:
        out["rule_version"] = data["ruleVersion"]
    if "expression" in data:
        out["expression"] = data["expression"]
    if "expressionWithValues" in data:
        out["expression_with_values"] = data["expressionWithValues"]
    if "outcomes" in data:
        import capo_frauddetector.types.list_of_strings

        out["outcomes"] = (
            capo_frauddetector.types.list_of_strings.deserialize_aws_json_1_1(
                data["outcomes"]
            )
        )
    if "evaluated" in data:
        out["evaluated"] = data["evaluated"]
    if "matched" in data:
        out["matched"] = data["matched"]
    return out
