"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleBooleanExpression``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.rule_boolean_operator
    import aws_sdk_mailmanager.types.rule_boolean_to_evaluate


class RuleBooleanExpression(TypedDict):
    evaluate: "aws_sdk_mailmanager.types.rule_boolean_to_evaluate.RuleBooleanToEvaluate"
    """<p>The operand on which to perform a boolean condition operation.</p>"""
    operator: "aws_sdk_mailmanager.types.rule_boolean_operator.RuleBooleanOperator"
    """<p>The matching operator for a boolean condition expression.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleBooleanExpression) -> dict:
    out: dict = {}
    import aws_sdk_mailmanager.types.rule_boolean_to_evaluate

    out["Evaluate"] = (
        aws_sdk_mailmanager.types.rule_boolean_to_evaluate.serialize_aws_json_1_0(
            value["evaluate"]
        )
    )
    import aws_sdk_mailmanager.types.rule_boolean_operator

    out["Operator"] = (
        aws_sdk_mailmanager.types.rule_boolean_operator.serialize_aws_json_1_0(
            value["operator"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> RuleBooleanExpression:
    out: RuleBooleanExpression = {}  # type: ignore[typeddict-item]
    if "Evaluate" in data:
        import aws_sdk_mailmanager.types.rule_boolean_to_evaluate

        out["evaluate"] = (
            aws_sdk_mailmanager.types.rule_boolean_to_evaluate.deserialize_aws_json_1_0(
                data["Evaluate"]
            )
        )
    else:
        raise DeserializationError("RuleBooleanExpression.evaluate required")
    if "Operator" in data:
        import aws_sdk_mailmanager.types.rule_boolean_operator

        out["operator"] = (
            aws_sdk_mailmanager.types.rule_boolean_operator.deserialize_aws_json_1_0(
                data["Operator"]
            )
        )
    else:
        raise DeserializationError("RuleBooleanExpression.operator required")
    return out
