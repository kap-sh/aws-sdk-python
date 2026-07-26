"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleNumberExpression``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mailmanager.types.rule_number_operator
    import capo_mailmanager.types.rule_number_to_evaluate


class RuleNumberExpression(TypedDict, closed=True):
    evaluate: "capo_mailmanager.types.rule_number_to_evaluate.RuleNumberToEvaluate"
    """<p>The number to evaluate in a numeric condition expression.</p>"""
    operator: "capo_mailmanager.types.rule_number_operator.RuleNumberOperator"
    """<p>The operator for a numeric condition expression.</p>"""
    value: "float"
    """<p>The value to evaluate in a numeric condition expression.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleNumberExpression) -> dict:
    out: dict = {}
    import capo_mailmanager.types.rule_number_to_evaluate

    out["Evaluate"] = (
        capo_mailmanager.types.rule_number_to_evaluate.serialize_aws_json_1_0(
            value["evaluate"]
        )
    )
    import capo_mailmanager.types.rule_number_operator

    out["Operator"] = (
        capo_mailmanager.types.rule_number_operator.serialize_aws_json_1_0(
            value["operator"]
        )
    )
    out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RuleNumberExpression:
    out: RuleNumberExpression = {}  # type: ignore[typeddict-item]
    if "Evaluate" in data:
        import capo_mailmanager.types.rule_number_to_evaluate

        out["evaluate"] = (
            capo_mailmanager.types.rule_number_to_evaluate.deserialize_aws_json_1_0(
                data["Evaluate"]
            )
        )
    else:
        raise DeserializationError("RuleNumberExpression.evaluate required")
    if "Operator" in data:
        import capo_mailmanager.types.rule_number_operator

        out["operator"] = (
            capo_mailmanager.types.rule_number_operator.deserialize_aws_json_1_0(
                data["Operator"]
            )
        )
    else:
        raise DeserializationError("RuleNumberExpression.operator required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("RuleNumberExpression.value required")
    return out
