"""Generated from Smithy shape ``com.amazonaws.mailmanager#IngressIpv6ToEvaluate``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_mailmanager.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.ingress_ipv6_attribute


class _IngressIpv6ToEvaluate_Attribute(TypedDict):
    Attribute: "aws_sdk_mailmanager.types.ingress_ipv6_attribute.IngressIpv6Attribute"


IngressIpv6ToEvaluate: TypeAlias = _IngressIpv6ToEvaluate_Attribute


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngressIpv6ToEvaluate) -> dict:
    if "Attribute" in value:
        import aws_sdk_mailmanager.types.ingress_ipv6_attribute

        return {
            "Attribute": aws_sdk_mailmanager.types.ingress_ipv6_attribute.serialize_aws_json_1_0(
                value["Attribute"]
            )
        }
    else:
        raise SerializationError("IngressIpv6ToEvaluate: no variant present")


def deserialize_aws_json_1_0(data: dict) -> IngressIpv6ToEvaluate:
    if "Attribute" in data:
        import aws_sdk_mailmanager.types.ingress_ipv6_attribute

        return {
            "Attribute": aws_sdk_mailmanager.types.ingress_ipv6_attribute.deserialize_aws_json_1_0(
                data["Attribute"]
            )
        }
    else:
        raise DeserializationError("IngressIpv6ToEvaluate: no recognized variant key")
