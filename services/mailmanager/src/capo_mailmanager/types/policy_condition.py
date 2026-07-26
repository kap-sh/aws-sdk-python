"""Generated from Smithy shape ``com.amazonaws.mailmanager#PolicyCondition``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mailmanager.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_mailmanager.types.ingress_boolean_expression
    import capo_mailmanager.types.ingress_ipv4_expression
    import capo_mailmanager.types.ingress_ipv6_expression
    import capo_mailmanager.types.ingress_string_expression
    import capo_mailmanager.types.ingress_tls_protocol_expression


class _PolicyCondition_StringExpression(TypedDict, closed=True):
    StringExpression: (
        "capo_mailmanager.types.ingress_string_expression.IngressStringExpression"
    )


class _PolicyCondition_IpExpression(TypedDict, closed=True):
    IpExpression: "capo_mailmanager.types.ingress_ipv4_expression.IngressIpv4Expression"


class _PolicyCondition_Ipv6Expression(TypedDict, closed=True):
    Ipv6Expression: (
        "capo_mailmanager.types.ingress_ipv6_expression.IngressIpv6Expression"
    )


class _PolicyCondition_TlsExpression(TypedDict, closed=True):
    TlsExpression: "capo_mailmanager.types.ingress_tls_protocol_expression.IngressTlsProtocolExpression"


class _PolicyCondition_BooleanExpression(TypedDict, closed=True):
    BooleanExpression: (
        "capo_mailmanager.types.ingress_boolean_expression.IngressBooleanExpression"
    )


PolicyCondition: TypeAlias = (
    _PolicyCondition_StringExpression
    | _PolicyCondition_IpExpression
    | _PolicyCondition_Ipv6Expression
    | _PolicyCondition_TlsExpression
    | _PolicyCondition_BooleanExpression
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PolicyCondition) -> dict:
    if "StringExpression" in value:
        import capo_mailmanager.types.ingress_string_expression

        return {
            "StringExpression": capo_mailmanager.types.ingress_string_expression.serialize_aws_json_1_0(
                value["StringExpression"]
            )
        }
    elif "IpExpression" in value:
        import capo_mailmanager.types.ingress_ipv4_expression

        return {
            "IpExpression": capo_mailmanager.types.ingress_ipv4_expression.serialize_aws_json_1_0(
                value["IpExpression"]
            )
        }
    elif "Ipv6Expression" in value:
        import capo_mailmanager.types.ingress_ipv6_expression

        return {
            "Ipv6Expression": capo_mailmanager.types.ingress_ipv6_expression.serialize_aws_json_1_0(
                value["Ipv6Expression"]
            )
        }
    elif "TlsExpression" in value:
        import capo_mailmanager.types.ingress_tls_protocol_expression

        return {
            "TlsExpression": capo_mailmanager.types.ingress_tls_protocol_expression.serialize_aws_json_1_0(
                value["TlsExpression"]
            )
        }
    elif "BooleanExpression" in value:
        import capo_mailmanager.types.ingress_boolean_expression

        return {
            "BooleanExpression": capo_mailmanager.types.ingress_boolean_expression.serialize_aws_json_1_0(
                value["BooleanExpression"]
            )
        }
    else:
        raise SerializationError("PolicyCondition: no variant present")


def deserialize_aws_json_1_0(data: dict) -> PolicyCondition:
    if "StringExpression" in data:
        import capo_mailmanager.types.ingress_string_expression

        return {
            "StringExpression": capo_mailmanager.types.ingress_string_expression.deserialize_aws_json_1_0(
                data["StringExpression"]
            )
        }
    elif "IpExpression" in data:
        import capo_mailmanager.types.ingress_ipv4_expression

        return {
            "IpExpression": capo_mailmanager.types.ingress_ipv4_expression.deserialize_aws_json_1_0(
                data["IpExpression"]
            )
        }
    elif "Ipv6Expression" in data:
        import capo_mailmanager.types.ingress_ipv6_expression

        return {
            "Ipv6Expression": capo_mailmanager.types.ingress_ipv6_expression.deserialize_aws_json_1_0(
                data["Ipv6Expression"]
            )
        }
    elif "TlsExpression" in data:
        import capo_mailmanager.types.ingress_tls_protocol_expression

        return {
            "TlsExpression": capo_mailmanager.types.ingress_tls_protocol_expression.deserialize_aws_json_1_0(
                data["TlsExpression"]
            )
        }
    elif "BooleanExpression" in data:
        import capo_mailmanager.types.ingress_boolean_expression

        return {
            "BooleanExpression": capo_mailmanager.types.ingress_boolean_expression.deserialize_aws_json_1_0(
                data["BooleanExpression"]
            )
        }
    else:
        raise DeserializationError("PolicyCondition: no recognized variant key")
