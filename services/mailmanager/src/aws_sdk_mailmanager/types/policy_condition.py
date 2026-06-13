"""Generated from Smithy shape ``com.amazonaws.mailmanager#PolicyCondition``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_mailmanager.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.ingress_boolean_expression
    import aws_sdk_mailmanager.types.ingress_ipv4_expression
    import aws_sdk_mailmanager.types.ingress_ipv6_expression
    import aws_sdk_mailmanager.types.ingress_string_expression
    import aws_sdk_mailmanager.types.ingress_tls_protocol_expression


class _PolicyCondition_StringExpression(TypedDict):
    StringExpression: (
        "aws_sdk_mailmanager.types.ingress_string_expression.IngressStringExpression"
    )


class _PolicyCondition_IpExpression(TypedDict):
    IpExpression: (
        "aws_sdk_mailmanager.types.ingress_ipv4_expression.IngressIpv4Expression"
    )


class _PolicyCondition_Ipv6Expression(TypedDict):
    Ipv6Expression: (
        "aws_sdk_mailmanager.types.ingress_ipv6_expression.IngressIpv6Expression"
    )


class _PolicyCondition_TlsExpression(TypedDict):
    TlsExpression: "aws_sdk_mailmanager.types.ingress_tls_protocol_expression.IngressTlsProtocolExpression"


class _PolicyCondition_BooleanExpression(TypedDict):
    BooleanExpression: (
        "aws_sdk_mailmanager.types.ingress_boolean_expression.IngressBooleanExpression"
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
        import aws_sdk_mailmanager.types.ingress_string_expression

        return {
            "StringExpression": aws_sdk_mailmanager.types.ingress_string_expression.serialize_aws_json_1_0(
                value["StringExpression"]
            )
        }
    elif "IpExpression" in value:
        import aws_sdk_mailmanager.types.ingress_ipv4_expression

        return {
            "IpExpression": aws_sdk_mailmanager.types.ingress_ipv4_expression.serialize_aws_json_1_0(
                value["IpExpression"]
            )
        }
    elif "Ipv6Expression" in value:
        import aws_sdk_mailmanager.types.ingress_ipv6_expression

        return {
            "Ipv6Expression": aws_sdk_mailmanager.types.ingress_ipv6_expression.serialize_aws_json_1_0(
                value["Ipv6Expression"]
            )
        }
    elif "TlsExpression" in value:
        import aws_sdk_mailmanager.types.ingress_tls_protocol_expression

        return {
            "TlsExpression": aws_sdk_mailmanager.types.ingress_tls_protocol_expression.serialize_aws_json_1_0(
                value["TlsExpression"]
            )
        }
    elif "BooleanExpression" in value:
        import aws_sdk_mailmanager.types.ingress_boolean_expression

        return {
            "BooleanExpression": aws_sdk_mailmanager.types.ingress_boolean_expression.serialize_aws_json_1_0(
                value["BooleanExpression"]
            )
        }
    else:
        raise SerializationError("PolicyCondition: no variant present")


def deserialize_aws_json_1_0(data: dict) -> PolicyCondition:
    if "StringExpression" in data:
        import aws_sdk_mailmanager.types.ingress_string_expression

        return {
            "StringExpression": aws_sdk_mailmanager.types.ingress_string_expression.deserialize_aws_json_1_0(
                data["StringExpression"]
            )
        }
    elif "IpExpression" in data:
        import aws_sdk_mailmanager.types.ingress_ipv4_expression

        return {
            "IpExpression": aws_sdk_mailmanager.types.ingress_ipv4_expression.deserialize_aws_json_1_0(
                data["IpExpression"]
            )
        }
    elif "Ipv6Expression" in data:
        import aws_sdk_mailmanager.types.ingress_ipv6_expression

        return {
            "Ipv6Expression": aws_sdk_mailmanager.types.ingress_ipv6_expression.deserialize_aws_json_1_0(
                data["Ipv6Expression"]
            )
        }
    elif "TlsExpression" in data:
        import aws_sdk_mailmanager.types.ingress_tls_protocol_expression

        return {
            "TlsExpression": aws_sdk_mailmanager.types.ingress_tls_protocol_expression.deserialize_aws_json_1_0(
                data["TlsExpression"]
            )
        }
    elif "BooleanExpression" in data:
        import aws_sdk_mailmanager.types.ingress_boolean_expression

        return {
            "BooleanExpression": aws_sdk_mailmanager.types.ingress_boolean_expression.deserialize_aws_json_1_0(
                data["BooleanExpression"]
            )
        }
    else:
        raise DeserializationError("PolicyCondition: no recognized variant key")
