"""Generated from Smithy shape ``com.amazonaws.servicediscovery#PublicDnsNamespaceChange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_servicediscovery.types.public_dns_namespace_properties_change
    import capo_servicediscovery.types.resource_description


class PublicDnsNamespaceChange(TypedDict, closed=True):
    description: NotRequired[
        "capo_servicediscovery.types.resource_description.ResourceDescription"
    ]
    """<p>An updated description for the public DNS namespace.</p>"""
    properties: NotRequired[
        "capo_servicediscovery.types.public_dns_namespace_properties_change.PublicDnsNamespacePropertiesChange"
    ]
    """<p>Properties to be updated in the public DNS namespace.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PublicDnsNamespaceChange) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "properties" in value:
        import capo_servicediscovery.types.public_dns_namespace_properties_change

        out["Properties"] = (
            capo_servicediscovery.types.public_dns_namespace_properties_change.serialize_aws_json_1_1(
                value["properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PublicDnsNamespaceChange:
    out: PublicDnsNamespaceChange = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Properties" in data:
        import capo_servicediscovery.types.public_dns_namespace_properties_change

        out["properties"] = (
            capo_servicediscovery.types.public_dns_namespace_properties_change.deserialize_aws_json_1_1(
                data["Properties"]
            )
        )
    return out
