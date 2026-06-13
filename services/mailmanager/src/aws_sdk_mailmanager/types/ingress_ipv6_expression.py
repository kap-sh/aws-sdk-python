"""Generated from Smithy shape ``com.amazonaws.mailmanager#IngressIpv6Expression``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.ingress_ip_operator
    import aws_sdk_mailmanager.types.ingress_ipv6_to_evaluate
    import aws_sdk_mailmanager.types.ipv6_cidrs


class IngressIpv6Expression(TypedDict):
    evaluate: "aws_sdk_mailmanager.types.ingress_ipv6_to_evaluate.IngressIpv6ToEvaluate"
    """<p>The left hand side argument of an IPv6 condition expression.</p>"""
    operator: "aws_sdk_mailmanager.types.ingress_ip_operator.IngressIpOperator"
    """<p>The matching operator for an IPv6 condition expression.</p>"""
    values: "aws_sdk_mailmanager.types.ipv6_cidrs.Ipv6Cidrs"
    """<p>The right hand side argument of an IPv6 condition expression.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngressIpv6Expression) -> dict:
    out: dict = {}
    import aws_sdk_mailmanager.types.ingress_ipv6_to_evaluate

    out["Evaluate"] = (
        aws_sdk_mailmanager.types.ingress_ipv6_to_evaluate.serialize_aws_json_1_0(
            value["evaluate"]
        )
    )
    import aws_sdk_mailmanager.types.ingress_ip_operator

    out["Operator"] = (
        aws_sdk_mailmanager.types.ingress_ip_operator.serialize_aws_json_1_0(
            value["operator"]
        )
    )
    import aws_sdk_mailmanager.types.ipv6_cidrs

    out["Values"] = aws_sdk_mailmanager.types.ipv6_cidrs.serialize_aws_json_1_0(
        value["values"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> IngressIpv6Expression:
    out: IngressIpv6Expression = {}  # type: ignore[typeddict-item]
    if "Evaluate" in data:
        import aws_sdk_mailmanager.types.ingress_ipv6_to_evaluate

        out["evaluate"] = (
            aws_sdk_mailmanager.types.ingress_ipv6_to_evaluate.deserialize_aws_json_1_0(
                data["Evaluate"]
            )
        )
    else:
        raise DeserializationError("IngressIpv6Expression.evaluate required")
    if "Operator" in data:
        import aws_sdk_mailmanager.types.ingress_ip_operator

        out["operator"] = (
            aws_sdk_mailmanager.types.ingress_ip_operator.deserialize_aws_json_1_0(
                data["Operator"]
            )
        )
    else:
        raise DeserializationError("IngressIpv6Expression.operator required")
    if "Values" in data:
        import aws_sdk_mailmanager.types.ipv6_cidrs

        out["values"] = aws_sdk_mailmanager.types.ipv6_cidrs.deserialize_aws_json_1_0(
            data["Values"]
        )
    else:
        raise DeserializationError("IngressIpv6Expression.values required")
    return out
