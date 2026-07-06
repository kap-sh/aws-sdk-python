"""Generated from Smithy shape ``com.amazonaws.mailmanager#IngressIpToEvaluate``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_mailmanager.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.ingress_ipv4_attribute


class _IngressIpToEvaluate_Attribute(TypedDict, closed=True):
    Attribute: "aws_sdk_mailmanager.types.ingress_ipv4_attribute.IngressIpv4Attribute"


IngressIpToEvaluate: TypeAlias = _IngressIpToEvaluate_Attribute


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngressIpToEvaluate) -> dict:
    if "Attribute" in value:
        import aws_sdk_mailmanager.types.ingress_ipv4_attribute

        return {
            "Attribute": aws_sdk_mailmanager.types.ingress_ipv4_attribute.serialize_aws_json_1_0(
                value["Attribute"]
            )
        }
    else:
        raise SerializationError("IngressIpToEvaluate: no variant present")


def deserialize_aws_json_1_0(data: dict) -> IngressIpToEvaluate:
    if "Attribute" in data:
        import aws_sdk_mailmanager.types.ingress_ipv4_attribute

        return {
            "Attribute": aws_sdk_mailmanager.types.ingress_ipv4_attribute.deserialize_aws_json_1_0(
                data["Attribute"]
            )
        }
    else:
        raise DeserializationError("IngressIpToEvaluate: no recognized variant key")
