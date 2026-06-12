"""Generated from Smithy shape ``com.amazonaws.servicediscovery#PrivateDnsNamespaceProperties``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_servicediscovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_servicediscovery.types.private_dns_properties_mutable


class PrivateDnsNamespaceProperties(TypedDict):
    dns_properties: "aws_sdk_servicediscovery.types.private_dns_properties_mutable.PrivateDnsPropertiesMutable"
    """<p>DNS properties for the private DNS namespace.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PrivateDnsNamespaceProperties) -> dict:
    out: dict = {}
    import aws_sdk_servicediscovery.types.private_dns_properties_mutable

    out["DnsProperties"] = (
        aws_sdk_servicediscovery.types.private_dns_properties_mutable.serialize_aws_json_1_1(
            value["dns_properties"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PrivateDnsNamespaceProperties:
    out: PrivateDnsNamespaceProperties = {}  # type: ignore[typeddict-item]
    if "DnsProperties" in data:
        import aws_sdk_servicediscovery.types.private_dns_properties_mutable

        out["dns_properties"] = (
            aws_sdk_servicediscovery.types.private_dns_properties_mutable.deserialize_aws_json_1_1(
                data["DnsProperties"]
            )
        )
    else:
        raise DeserializationError(
            "PrivateDnsNamespaceProperties.dns_properties required"
        )
    return out
