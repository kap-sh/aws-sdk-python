"""Generated from Smithy shape ``com.amazonaws.ram#Resource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ram.types.date_time
    import aws_sdk_ram.types.resource_region_scope
    import aws_sdk_ram.types.resource_status
    import aws_sdk_ram.types.string


class Resource(TypedDict):
    arn: NotRequired["aws_sdk_ram.types.string.String"]
    r"""<p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Name (ARN)</a> of the resource.</p>"""
    type: NotRequired["aws_sdk_ram.types.string.String"]
    """<p>The resource type. This takes the form of: <code>service-code</code>:<code>resource-code</code>, and is case-insensitive. For example, an Amazon EC2 Subnet would be represented by the string <code>ec2:subnet</code>.</p>"""
    resource_share_arn: NotRequired["aws_sdk_ram.types.string.String"]
    r"""<p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Name (ARN)</a> of the resource share this resource is associated with.</p>"""
    resource_group_arn: NotRequired["aws_sdk_ram.types.string.String"]
    r"""<p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Name (ARN)</a> of the resource group. This value is available only if the resource is part of a resource group.</p>"""
    status: NotRequired["aws_sdk_ram.types.resource_status.ResourceStatus"]
    """<p>The current status of the resource.</p>"""
    status_message: NotRequired["aws_sdk_ram.types.string.String"]
    """<p>A message about the status of the resource.</p>"""
    creation_time: NotRequired["aws_sdk_ram.types.date_time.DateTime"]
    """<p>The date and time when the resource was associated with the resource share.</p>"""
    last_updated_time: NotRequired["aws_sdk_ram.types.date_time.DateTime"]
    """<p>The date an time when the association between the resource and the resource share was last updated.</p>"""
    resource_region_scope: NotRequired[
        "aws_sdk_ram.types.resource_region_scope.ResourceRegionScope"
    ]
    """<p>Specifies the scope of visibility of this resource:</p> <ul> <li> <p> <b>REGIONAL</b> – The resource can be accessed only by using requests that target the Amazon Web Services Region in which the resource exists.</p> </li> <li> <p> <b>GLOBAL</b> – The resource can be accessed from any Amazon Web Services Region.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: Resource) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "type" in value:
        out["type"] = value["type"]
    if "resource_share_arn" in value:
        out["resourceShareArn"] = value["resource_share_arn"]
    if "resource_group_arn" in value:
        out["resourceGroupArn"] = value["resource_group_arn"]
    if "status" in value:
        import aws_sdk_ram.types.resource_status

        out["status"] = aws_sdk_ram.types.resource_status.serialize_json(
            value["status"]
        )
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "creation_time" in value:
        import aws_sdk_ram.types.date_time

        out["creationTime"] = aws_sdk_ram.types.date_time.serialize_json(
            value["creation_time"]
        )
    if "last_updated_time" in value:
        import aws_sdk_ram.types.date_time

        out["lastUpdatedTime"] = aws_sdk_ram.types.date_time.serialize_json(
            value["last_updated_time"]
        )
    if "resource_region_scope" in value:
        import aws_sdk_ram.types.resource_region_scope

        out["resourceRegionScope"] = (
            aws_sdk_ram.types.resource_region_scope.serialize_json(
                value["resource_region_scope"]
            )
        )
    return out


def deserialize_json(data: dict) -> Resource:
    out: Resource = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "type" in data:
        out["type"] = data["type"]
    if "resourceShareArn" in data:
        out["resource_share_arn"] = data["resourceShareArn"]
    if "resourceGroupArn" in data:
        out["resource_group_arn"] = data["resourceGroupArn"]
    if "status" in data:
        import aws_sdk_ram.types.resource_status

        out["status"] = aws_sdk_ram.types.resource_status.deserialize_json(
            data["status"]
        )
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    if "creationTime" in data:
        import aws_sdk_ram.types.date_time

        out["creation_time"] = aws_sdk_ram.types.date_time.deserialize_json(
            data["creationTime"]
        )
    if "lastUpdatedTime" in data:
        import aws_sdk_ram.types.date_time

        out["last_updated_time"] = aws_sdk_ram.types.date_time.deserialize_json(
            data["lastUpdatedTime"]
        )
    if "resourceRegionScope" in data:
        import aws_sdk_ram.types.resource_region_scope

        out["resource_region_scope"] = (
            aws_sdk_ram.types.resource_region_scope.deserialize_json(
                data["resourceRegionScope"]
            )
        )
    return out
