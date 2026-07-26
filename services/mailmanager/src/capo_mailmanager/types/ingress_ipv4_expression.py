"""Generated from Smithy shape ``com.amazonaws.mailmanager#IngressIpv4Expression``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mailmanager.types.ingress_ip_operator
    import capo_mailmanager.types.ingress_ip_to_evaluate
    import capo_mailmanager.types.ipv4_cidrs


class IngressIpv4Expression(TypedDict, closed=True):
    evaluate: "capo_mailmanager.types.ingress_ip_to_evaluate.IngressIpToEvaluate"
    """<p>The left hand side argument of an IP condition expression.</p>"""
    operator: "capo_mailmanager.types.ingress_ip_operator.IngressIpOperator"
    """<p>The matching operator for an IP condition expression.</p>"""
    values: "capo_mailmanager.types.ipv4_cidrs.Ipv4Cidrs"
    """<p>The right hand side argument of an IP condition expression.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngressIpv4Expression) -> dict:
    out: dict = {}
    import capo_mailmanager.types.ingress_ip_to_evaluate

    out["Evaluate"] = (
        capo_mailmanager.types.ingress_ip_to_evaluate.serialize_aws_json_1_0(
            value["evaluate"]
        )
    )
    import capo_mailmanager.types.ingress_ip_operator

    out["Operator"] = capo_mailmanager.types.ingress_ip_operator.serialize_aws_json_1_0(
        value["operator"]
    )
    import capo_mailmanager.types.ipv4_cidrs

    out["Values"] = capo_mailmanager.types.ipv4_cidrs.serialize_aws_json_1_0(
        value["values"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> IngressIpv4Expression:
    out: IngressIpv4Expression = {}  # type: ignore[typeddict-item]
    if "Evaluate" in data:
        import capo_mailmanager.types.ingress_ip_to_evaluate

        out["evaluate"] = (
            capo_mailmanager.types.ingress_ip_to_evaluate.deserialize_aws_json_1_0(
                data["Evaluate"]
            )
        )
    else:
        raise DeserializationError("IngressIpv4Expression.evaluate required")
    if "Operator" in data:
        import capo_mailmanager.types.ingress_ip_operator

        out["operator"] = (
            capo_mailmanager.types.ingress_ip_operator.deserialize_aws_json_1_0(
                data["Operator"]
            )
        )
    else:
        raise DeserializationError("IngressIpv4Expression.operator required")
    if "Values" in data:
        import capo_mailmanager.types.ipv4_cidrs

        out["values"] = capo_mailmanager.types.ipv4_cidrs.deserialize_aws_json_1_0(
            data["Values"]
        )
    else:
        raise DeserializationError("IngressIpv4Expression.values required")
    return out
