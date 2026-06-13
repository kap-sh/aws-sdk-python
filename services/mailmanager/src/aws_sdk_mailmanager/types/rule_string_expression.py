"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleStringExpression``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.rule_string_list
    import aws_sdk_mailmanager.types.rule_string_operator
    import aws_sdk_mailmanager.types.rule_string_to_evaluate


class RuleStringExpression(TypedDict):
    evaluate: "aws_sdk_mailmanager.types.rule_string_to_evaluate.RuleStringToEvaluate"
    """<p>The string to evaluate in a string condition expression.</p>"""
    operator: "aws_sdk_mailmanager.types.rule_string_operator.RuleStringOperator"
    """<p>The matching operator for a string condition expression.</p>"""
    values: "aws_sdk_mailmanager.types.rule_string_list.RuleStringList"
    """<p>The string(s) to be evaluated in a string condition expression. For all operators, except for NOT_EQUALS, if multiple values are given, the values are processed as an OR. That is, if any of the values match the email's string using the given operator, the condition is deemed to match. However, for NOT_EQUALS, the condition is only deemed to match if none of the given strings match the email's string.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleStringExpression) -> dict:
    out: dict = {}
    import aws_sdk_mailmanager.types.rule_string_to_evaluate

    out["Evaluate"] = (
        aws_sdk_mailmanager.types.rule_string_to_evaluate.serialize_aws_json_1_0(
            value["evaluate"]
        )
    )
    import aws_sdk_mailmanager.types.rule_string_operator

    out["Operator"] = (
        aws_sdk_mailmanager.types.rule_string_operator.serialize_aws_json_1_0(
            value["operator"]
        )
    )
    import aws_sdk_mailmanager.types.rule_string_list

    out["Values"] = aws_sdk_mailmanager.types.rule_string_list.serialize_aws_json_1_0(
        value["values"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> RuleStringExpression:
    out: RuleStringExpression = {}  # type: ignore[typeddict-item]
    if "Evaluate" in data:
        import aws_sdk_mailmanager.types.rule_string_to_evaluate

        out["evaluate"] = (
            aws_sdk_mailmanager.types.rule_string_to_evaluate.deserialize_aws_json_1_0(
                data["Evaluate"]
            )
        )
    else:
        raise DeserializationError("RuleStringExpression.evaluate required")
    if "Operator" in data:
        import aws_sdk_mailmanager.types.rule_string_operator

        out["operator"] = (
            aws_sdk_mailmanager.types.rule_string_operator.deserialize_aws_json_1_0(
                data["Operator"]
            )
        )
    else:
        raise DeserializationError("RuleStringExpression.operator required")
    if "Values" in data:
        import aws_sdk_mailmanager.types.rule_string_list

        out["values"] = (
            aws_sdk_mailmanager.types.rule_string_list.deserialize_aws_json_1_0(
                data["Values"]
            )
        )
    else:
        raise DeserializationError("RuleStringExpression.values required")
    return out
