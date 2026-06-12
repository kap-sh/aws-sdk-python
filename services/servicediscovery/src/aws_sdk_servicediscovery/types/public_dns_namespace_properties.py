"""Generated from Smithy shape ``com.amazonaws.servicediscovery#PublicDnsNamespaceProperties``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_servicediscovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_servicediscovery.types.public_dns_properties_mutable


class PublicDnsNamespaceProperties(TypedDict):
    dns_properties: "aws_sdk_servicediscovery.types.public_dns_properties_mutable.PublicDnsPropertiesMutable"
    """<p>DNS properties for the public DNS namespace.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PublicDnsNamespaceProperties) -> dict:
    out: dict = {}
    import aws_sdk_servicediscovery.types.public_dns_properties_mutable

    out["DnsProperties"] = (
        aws_sdk_servicediscovery.types.public_dns_properties_mutable.serialize_aws_json_1_1(
            value["dns_properties"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PublicDnsNamespaceProperties:
    out: PublicDnsNamespaceProperties = {}  # type: ignore[typeddict-item]
    if "DnsProperties" in data:
        import aws_sdk_servicediscovery.types.public_dns_properties_mutable

        out["dns_properties"] = (
            aws_sdk_servicediscovery.types.public_dns_properties_mutable.deserialize_aws_json_1_1(
                data["DnsProperties"]
            )
        )
    else:
        raise DeserializationError(
            "PublicDnsNamespaceProperties.dns_properties required"
        )
    return out
