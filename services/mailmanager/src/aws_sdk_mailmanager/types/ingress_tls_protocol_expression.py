"""Generated from Smithy shape ``com.amazonaws.mailmanager#IngressTlsProtocolExpression``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.ingress_tls_protocol_attribute
    import aws_sdk_mailmanager.types.ingress_tls_protocol_operator
    import aws_sdk_mailmanager.types.ingress_tls_protocol_to_evaluate


class IngressTlsProtocolExpression(TypedDict, closed=True):
    evaluate: "aws_sdk_mailmanager.types.ingress_tls_protocol_to_evaluate.IngressTlsProtocolToEvaluate"
    """<p>The left hand side argument of a TLS condition expression.</p>"""
    operator: "aws_sdk_mailmanager.types.ingress_tls_protocol_operator.IngressTlsProtocolOperator"
    """<p>The matching operator for a TLS condition expression.</p>"""
    value: "aws_sdk_mailmanager.types.ingress_tls_protocol_attribute.IngressTlsProtocolAttribute"
    """<p>The right hand side argument of a TLS condition expression.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngressTlsProtocolExpression) -> dict:
    out: dict = {}
    import aws_sdk_mailmanager.types.ingress_tls_protocol_to_evaluate

    out["Evaluate"] = (
        aws_sdk_mailmanager.types.ingress_tls_protocol_to_evaluate.serialize_aws_json_1_0(
            value["evaluate"]
        )
    )
    import aws_sdk_mailmanager.types.ingress_tls_protocol_operator

    out["Operator"] = (
        aws_sdk_mailmanager.types.ingress_tls_protocol_operator.serialize_aws_json_1_0(
            value["operator"]
        )
    )
    import aws_sdk_mailmanager.types.ingress_tls_protocol_attribute

    out["Value"] = (
        aws_sdk_mailmanager.types.ingress_tls_protocol_attribute.serialize_aws_json_1_0(
            value["value"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> IngressTlsProtocolExpression:
    out: IngressTlsProtocolExpression = {}  # type: ignore[typeddict-item]
    if "Evaluate" in data:
        import aws_sdk_mailmanager.types.ingress_tls_protocol_to_evaluate

        out["evaluate"] = (
            aws_sdk_mailmanager.types.ingress_tls_protocol_to_evaluate.deserialize_aws_json_1_0(
                data["Evaluate"]
            )
        )
    else:
        raise DeserializationError("IngressTlsProtocolExpression.evaluate required")
    if "Operator" in data:
        import aws_sdk_mailmanager.types.ingress_tls_protocol_operator

        out["operator"] = (
            aws_sdk_mailmanager.types.ingress_tls_protocol_operator.deserialize_aws_json_1_0(
                data["Operator"]
            )
        )
    else:
        raise DeserializationError("IngressTlsProtocolExpression.operator required")
    if "Value" in data:
        import aws_sdk_mailmanager.types.ingress_tls_protocol_attribute

        out["value"] = (
            aws_sdk_mailmanager.types.ingress_tls_protocol_attribute.deserialize_aws_json_1_0(
                data["Value"]
            )
        )
    else:
        raise DeserializationError("IngressTlsProtocolExpression.value required")
    return out
