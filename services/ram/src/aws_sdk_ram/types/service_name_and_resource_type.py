"""Generated from Smithy shape ``com.amazonaws.ram#ServiceNameAndResourceType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ram.types.resource_region_scope
    import aws_sdk_ram.types.string


class ServiceNameAndResourceType(TypedDict, closed=True):
    resource_type: NotRequired["aws_sdk_ram.types.string.String"]
    """<p>The type of the resource. This takes the form of: <code>service-code</code>:<code>resource-code</code>, and is case-insensitive. For example, an Amazon EC2 Subnet would be represented by the string <code>ec2:subnet</code>.</p>"""
    service_name: NotRequired["aws_sdk_ram.types.string.String"]
    """<p>The name of the Amazon Web Services service to which resources of this type belong.</p>"""
    resource_region_scope: NotRequired[
        "aws_sdk_ram.types.resource_region_scope.ResourceRegionScope"
    ]
    """<p>Specifies the scope of visibility of resources of this type:</p> <ul> <li> <p> <b>REGIONAL</b> – The resource can be accessed only by using requests that target the Amazon Web Services Region in which the resource exists.</p> </li> <li> <p> <b>GLOBAL</b> – The resource can be accessed from any Amazon Web Services Region.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceNameAndResourceType) -> dict:
    out: dict = {}
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    if "service_name" in value:
        out["serviceName"] = value["service_name"]
    if "resource_region_scope" in value:
        import aws_sdk_ram.types.resource_region_scope

        out["resourceRegionScope"] = (
            aws_sdk_ram.types.resource_region_scope.serialize_json(
                value["resource_region_scope"]
            )
        )
    return out


def deserialize_json(data: dict) -> ServiceNameAndResourceType:
    out: ServiceNameAndResourceType = {}  # type: ignore[typeddict-item]
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    if "serviceName" in data:
        out["service_name"] = data["serviceName"]
    if "resourceRegionScope" in data:
        import aws_sdk_ram.types.resource_region_scope

        out["resource_region_scope"] = (
            aws_sdk_ram.types.resource_region_scope.deserialize_json(
                data["resourceRegionScope"]
            )
        )
    return out
