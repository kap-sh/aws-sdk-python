"""Generated from Smithy shape ``com.amazonaws.mailmanager#IngressTlsProtocolToEvaluate``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_mailmanager.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.ingress_tls_attribute


class _IngressTlsProtocolToEvaluate_Attribute(TypedDict, closed=True):
    Attribute: "aws_sdk_mailmanager.types.ingress_tls_attribute.IngressTlsAttribute"


IngressTlsProtocolToEvaluate: TypeAlias = _IngressTlsProtocolToEvaluate_Attribute


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngressTlsProtocolToEvaluate) -> dict:
    if "Attribute" in value:
        import aws_sdk_mailmanager.types.ingress_tls_attribute

        return {
            "Attribute": aws_sdk_mailmanager.types.ingress_tls_attribute.serialize_aws_json_1_0(
                value["Attribute"]
            )
        }
    else:
        raise SerializationError("IngressTlsProtocolToEvaluate: no variant present")


def deserialize_aws_json_1_0(data: dict) -> IngressTlsProtocolToEvaluate:
    if "Attribute" in data:
        import aws_sdk_mailmanager.types.ingress_tls_attribute

        return {
            "Attribute": aws_sdk_mailmanager.types.ingress_tls_attribute.deserialize_aws_json_1_0(
                data["Attribute"]
            )
        }
    else:
        raise DeserializationError(
            "IngressTlsProtocolToEvaluate: no recognized variant key"
        )
