"""Generated from Smithy shape ``com.amazonaws.mailmanager#IngressBooleanExpression``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.ingress_boolean_operator
    import aws_sdk_mailmanager.types.ingress_boolean_to_evaluate


class IngressBooleanExpression(TypedDict):
    evaluate: (
        "aws_sdk_mailmanager.types.ingress_boolean_to_evaluate.IngressBooleanToEvaluate"
    )
    """<p>The operand on which to perform a boolean condition operation.</p>"""
    operator: (
        "aws_sdk_mailmanager.types.ingress_boolean_operator.IngressBooleanOperator"
    )
    """<p>The matching operator for a boolean condition expression.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngressBooleanExpression) -> dict:
    out: dict = {}
    import aws_sdk_mailmanager.types.ingress_boolean_to_evaluate

    out["Evaluate"] = (
        aws_sdk_mailmanager.types.ingress_boolean_to_evaluate.serialize_aws_json_1_0(
            value["evaluate"]
        )
    )
    import aws_sdk_mailmanager.types.ingress_boolean_operator

    out["Operator"] = (
        aws_sdk_mailmanager.types.ingress_boolean_operator.serialize_aws_json_1_0(
            value["operator"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> IngressBooleanExpression:
    out: IngressBooleanExpression = {}  # type: ignore[typeddict-item]
    if "Evaluate" in data:
        import aws_sdk_mailmanager.types.ingress_boolean_to_evaluate

        out["evaluate"] = (
            aws_sdk_mailmanager.types.ingress_boolean_to_evaluate.deserialize_aws_json_1_0(
                data["Evaluate"]
            )
        )
    else:
        raise DeserializationError("IngressBooleanExpression.evaluate required")
    if "Operator" in data:
        import aws_sdk_mailmanager.types.ingress_boolean_operator

        out["operator"] = (
            aws_sdk_mailmanager.types.ingress_boolean_operator.deserialize_aws_json_1_0(
                data["Operator"]
            )
        )
    else:
        raise DeserializationError("IngressBooleanExpression.operator required")
    return out
