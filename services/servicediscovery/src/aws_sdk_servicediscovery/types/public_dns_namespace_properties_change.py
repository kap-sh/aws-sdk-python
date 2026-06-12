"""Generated from Smithy shape ``com.amazonaws.servicediscovery#PublicDnsNamespacePropertiesChange``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_servicediscovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_servicediscovery.types.public_dns_properties_mutable_change


class PublicDnsNamespacePropertiesChange(TypedDict):
    dns_properties: "aws_sdk_servicediscovery.types.public_dns_properties_mutable_change.PublicDnsPropertiesMutableChange"
    """<p>Updated DNS properties for the hosted zone for the public DNS namespace.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PublicDnsNamespacePropertiesChange) -> dict:
    out: dict = {}
    import aws_sdk_servicediscovery.types.public_dns_properties_mutable_change

    out["DnsProperties"] = (
        aws_sdk_servicediscovery.types.public_dns_properties_mutable_change.serialize_aws_json_1_1(
            value["dns_properties"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PublicDnsNamespacePropertiesChange:
    out: PublicDnsNamespacePropertiesChange = {}  # type: ignore[typeddict-item]
    if "DnsProperties" in data:
        import aws_sdk_servicediscovery.types.public_dns_properties_mutable_change

        out["dns_properties"] = (
            aws_sdk_servicediscovery.types.public_dns_properties_mutable_change.deserialize_aws_json_1_1(
                data["DnsProperties"]
            )
        )
    else:
        raise DeserializationError(
            "PublicDnsNamespacePropertiesChange.dns_properties required"
        )
    return out
