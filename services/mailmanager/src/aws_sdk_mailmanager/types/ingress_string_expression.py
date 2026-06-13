"""Generated from Smithy shape ``com.amazonaws.mailmanager#IngressStringExpression``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.ingress_string_operator
    import aws_sdk_mailmanager.types.ingress_string_to_evaluate
    import aws_sdk_mailmanager.types.string_list


class IngressStringExpression(TypedDict):
    evaluate: (
        "aws_sdk_mailmanager.types.ingress_string_to_evaluate.IngressStringToEvaluate"
    )
    """<p>The left hand side argument of a string condition expression.</p>"""
    operator: "aws_sdk_mailmanager.types.ingress_string_operator.IngressStringOperator"
    """<p>The matching operator for a string condition expression.</p>"""
    values: "aws_sdk_mailmanager.types.string_list.StringList"
    """<p>The right hand side argument of a string condition expression.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngressStringExpression) -> dict:
    out: dict = {}
    import aws_sdk_mailmanager.types.ingress_string_to_evaluate

    out["Evaluate"] = (
        aws_sdk_mailmanager.types.ingress_string_to_evaluate.serialize_aws_json_1_0(
            value["evaluate"]
        )
    )
    import aws_sdk_mailmanager.types.ingress_string_operator

    out["Operator"] = (
        aws_sdk_mailmanager.types.ingress_string_operator.serialize_aws_json_1_0(
            value["operator"]
        )
    )
    import aws_sdk_mailmanager.types.string_list

    out["Values"] = aws_sdk_mailmanager.types.string_list.serialize_aws_json_1_0(
        value["values"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> IngressStringExpression:
    out: IngressStringExpression = {}  # type: ignore[typeddict-item]
    if "Evaluate" in data:
        import aws_sdk_mailmanager.types.ingress_string_to_evaluate

        out["evaluate"] = (
            aws_sdk_mailmanager.types.ingress_string_to_evaluate.deserialize_aws_json_1_0(
                data["Evaluate"]
            )
        )
    else:
        raise DeserializationError("IngressStringExpression.evaluate required")
    if "Operator" in data:
        import aws_sdk_mailmanager.types.ingress_string_operator

        out["operator"] = (
            aws_sdk_mailmanager.types.ingress_string_operator.deserialize_aws_json_1_0(
                data["Operator"]
            )
        )
    else:
        raise DeserializationError("IngressStringExpression.operator required")
    if "Values" in data:
        import aws_sdk_mailmanager.types.string_list

        out["values"] = aws_sdk_mailmanager.types.string_list.deserialize_aws_json_1_0(
            data["Values"]
        )
    else:
        raise DeserializationError("IngressStringExpression.values required")
    return out
