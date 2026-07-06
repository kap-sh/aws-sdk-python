"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ResourceTargetDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.property_name
    import aws_sdk_service_catalog.types.requires_recreation
    import aws_sdk_service_catalog.types.resource_attribute


class ResourceTargetDefinition(TypedDict, closed=True):
    attribute: NotRequired[
        "aws_sdk_service_catalog.types.resource_attribute.ResourceAttribute"
    ]
    """<p>The attribute to be changed.</p>"""
    name: NotRequired["aws_sdk_service_catalog.types.property_name.PropertyName"]
    """<p>If the attribute is <code>Properties</code>, the value is the name of the property. Otherwise, the value is null.</p>"""
    requires_recreation: NotRequired[
        "aws_sdk_service_catalog.types.requires_recreation.RequiresRecreation"
    ]
    """<p>If the attribute is <code>Properties</code>, indicates whether a change to this property causes the resource to be re-created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceTargetDefinition) -> dict:
    out: dict = {}
    if "attribute" in value:
        import aws_sdk_service_catalog.types.resource_attribute

        out["Attribute"] = (
            aws_sdk_service_catalog.types.resource_attribute.serialize_aws_json_1_1(
                value["attribute"]
            )
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "requires_recreation" in value:
        import aws_sdk_service_catalog.types.requires_recreation

        out["RequiresRecreation"] = (
            aws_sdk_service_catalog.types.requires_recreation.serialize_aws_json_1_1(
                value["requires_recreation"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceTargetDefinition:
    out: ResourceTargetDefinition = {}  # type: ignore[typeddict-item]
    if "Attribute" in data:
        import aws_sdk_service_catalog.types.resource_attribute

        out["attribute"] = (
            aws_sdk_service_catalog.types.resource_attribute.deserialize_aws_json_1_1(
                data["Attribute"]
            )
        )
    if "Name" in data:
        out["name"] = data["Name"]
    if "RequiresRecreation" in data:
        import aws_sdk_service_catalog.types.requires_recreation

        out["requires_recreation"] = (
            aws_sdk_service_catalog.types.requires_recreation.deserialize_aws_json_1_1(
                data["RequiresRecreation"]
            )
        )
    return out
