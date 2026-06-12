"""Generated from Smithy shape ``com.amazonaws.servicediscovery#PrivateDnsNamespaceChange``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_servicediscovery.types.private_dns_namespace_properties_change
    import aws_sdk_servicediscovery.types.resource_description


class PrivateDnsNamespaceChange(TypedDict):
    description: NotRequired[
        "aws_sdk_servicediscovery.types.resource_description.ResourceDescription"
    ]
    """<p>An updated description for the private DNS namespace.</p>"""
    properties: NotRequired[
        "aws_sdk_servicediscovery.types.private_dns_namespace_properties_change.PrivateDnsNamespacePropertiesChange"
    ]
    """<p>Properties to be updated in the private DNS namespace.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PrivateDnsNamespaceChange) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "properties" in value:
        import aws_sdk_servicediscovery.types.private_dns_namespace_properties_change

        out["Properties"] = (
            aws_sdk_servicediscovery.types.private_dns_namespace_properties_change.serialize_aws_json_1_1(
                value["properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PrivateDnsNamespaceChange:
    out: PrivateDnsNamespaceChange = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Properties" in data:
        import aws_sdk_servicediscovery.types.private_dns_namespace_properties_change

        out["properties"] = (
            aws_sdk_servicediscovery.types.private_dns_namespace_properties_change.deserialize_aws_json_1_1(
                data["Properties"]
            )
        )
    return out
