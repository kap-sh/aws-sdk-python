"""Generated from Smithy shape ``com.amazonaws.mailmanager#IngressIpv6ToEvaluate``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mailmanager.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_mailmanager.types.ingress_ipv6_attribute


class _IngressIpv6ToEvaluate_Attribute(TypedDict, closed=True):
    Attribute: "capo_mailmanager.types.ingress_ipv6_attribute.IngressIpv6Attribute"


IngressIpv6ToEvaluate: TypeAlias = _IngressIpv6ToEvaluate_Attribute


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngressIpv6ToEvaluate) -> dict:
    if "Attribute" in value:
        import capo_mailmanager.types.ingress_ipv6_attribute

        return {
            "Attribute": capo_mailmanager.types.ingress_ipv6_attribute.serialize_aws_json_1_0(
                value["Attribute"]
            )
        }
    else:
        raise SerializationError("IngressIpv6ToEvaluate: no variant present")


def deserialize_aws_json_1_0(data: dict) -> IngressIpv6ToEvaluate:
    if "Attribute" in data:
        import capo_mailmanager.types.ingress_ipv6_attribute

        return {
            "Attribute": capo_mailmanager.types.ingress_ipv6_attribute.deserialize_aws_json_1_0(
                data["Attribute"]
            )
        }
    else:
        raise DeserializationError("IngressIpv6ToEvaluate: no recognized variant key")
