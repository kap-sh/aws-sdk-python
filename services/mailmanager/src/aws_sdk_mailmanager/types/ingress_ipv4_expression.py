"""Generated from Smithy shape ``com.amazonaws.mailmanager#IngressIpv4Expression``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.ingress_ip_operator
    import aws_sdk_mailmanager.types.ingress_ip_to_evaluate
    import aws_sdk_mailmanager.types.ipv4_cidrs


class IngressIpv4Expression(TypedDict, closed=True):
    evaluate: "aws_sdk_mailmanager.types.ingress_ip_to_evaluate.IngressIpToEvaluate"
    """<p>The left hand side argument of an IP condition expression.</p>"""
    operator: "aws_sdk_mailmanager.types.ingress_ip_operator.IngressIpOperator"
    """<p>The matching operator for an IP condition expression.</p>"""
    values: "aws_sdk_mailmanager.types.ipv4_cidrs.Ipv4Cidrs"
    """<p>The right hand side argument of an IP condition expression.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngressIpv4Expression) -> dict:
    out: dict = {}
    import aws_sdk_mailmanager.types.ingress_ip_to_evaluate

    out["Evaluate"] = (
        aws_sdk_mailmanager.types.ingress_ip_to_evaluate.serialize_aws_json_1_0(
            value["evaluate"]
        )
    )
    import aws_sdk_mailmanager.types.ingress_ip_operator

    out["Operator"] = (
        aws_sdk_mailmanager.types.ingress_ip_operator.serialize_aws_json_1_0(
            value["operator"]
        )
    )
    import aws_sdk_mailmanager.types.ipv4_cidrs

    out["Values"] = aws_sdk_mailmanager.types.ipv4_cidrs.serialize_aws_json_1_0(
        value["values"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> IngressIpv4Expression:
    out: IngressIpv4Expression = {}  # type: ignore[typeddict-item]
    if "Evaluate" in data:
        import aws_sdk_mailmanager.types.ingress_ip_to_evaluate

        out["evaluate"] = (
            aws_sdk_mailmanager.types.ingress_ip_to_evaluate.deserialize_aws_json_1_0(
                data["Evaluate"]
            )
        )
    else:
        raise DeserializationError("IngressIpv4Expression.evaluate required")
    if "Operator" in data:
        import aws_sdk_mailmanager.types.ingress_ip_operator

        out["operator"] = (
            aws_sdk_mailmanager.types.ingress_ip_operator.deserialize_aws_json_1_0(
                data["Operator"]
            )
        )
    else:
        raise DeserializationError("IngressIpv4Expression.operator required")
    if "Values" in data:
        import aws_sdk_mailmanager.types.ipv4_cidrs

        out["values"] = aws_sdk_mailmanager.types.ipv4_cidrs.deserialize_aws_json_1_0(
            data["Values"]
        )
    else:
        raise DeserializationError("IngressIpv4Expression.values required")
    return out
