"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleVerdictExpression``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.rule_verdict_operator
    import aws_sdk_mailmanager.types.rule_verdict_to_evaluate
    import aws_sdk_mailmanager.types.rule_verdict_value_list


class RuleVerdictExpression(TypedDict):
    evaluate: "aws_sdk_mailmanager.types.rule_verdict_to_evaluate.RuleVerdictToEvaluate"
    """<p>The verdict to evaluate in a verdict condition expression.</p>"""
    operator: "aws_sdk_mailmanager.types.rule_verdict_operator.RuleVerdictOperator"
    """<p>The matching operator for a verdict condition expression.</p>"""
    values: "aws_sdk_mailmanager.types.rule_verdict_value_list.RuleVerdictValueList"
    """<p>The values to match with the email's verdict using the given operator. For the EQUALS operator, if multiple values are given, the condition is deemed to match if any of the given verdicts match that of the email. For the NOT_EQUALS operator, if multiple values are given, the condition is deemed to match of none of the given verdicts match the verdict of the email.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleVerdictExpression) -> dict:
    out: dict = {}
    import aws_sdk_mailmanager.types.rule_verdict_to_evaluate

    out["Evaluate"] = (
        aws_sdk_mailmanager.types.rule_verdict_to_evaluate.serialize_aws_json_1_0(
            value["evaluate"]
        )
    )
    import aws_sdk_mailmanager.types.rule_verdict_operator

    out["Operator"] = (
        aws_sdk_mailmanager.types.rule_verdict_operator.serialize_aws_json_1_0(
            value["operator"]
        )
    )
    import aws_sdk_mailmanager.types.rule_verdict_value_list

    out["Values"] = (
        aws_sdk_mailmanager.types.rule_verdict_value_list.serialize_aws_json_1_0(
            value["values"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> RuleVerdictExpression:
    out: RuleVerdictExpression = {}  # type: ignore[typeddict-item]
    if "Evaluate" in data:
        import aws_sdk_mailmanager.types.rule_verdict_to_evaluate

        out["evaluate"] = (
            aws_sdk_mailmanager.types.rule_verdict_to_evaluate.deserialize_aws_json_1_0(
                data["Evaluate"]
            )
        )
    else:
        raise DeserializationError("RuleVerdictExpression.evaluate required")
    if "Operator" in data:
        import aws_sdk_mailmanager.types.rule_verdict_operator

        out["operator"] = (
            aws_sdk_mailmanager.types.rule_verdict_operator.deserialize_aws_json_1_0(
                data["Operator"]
            )
        )
    else:
        raise DeserializationError("RuleVerdictExpression.operator required")
    if "Values" in data:
        import aws_sdk_mailmanager.types.rule_verdict_value_list

        out["values"] = (
            aws_sdk_mailmanager.types.rule_verdict_value_list.deserialize_aws_json_1_0(
                data["Values"]
            )
        )
    else:
        raise DeserializationError("RuleVerdictExpression.values required")
    return out
