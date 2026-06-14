"""Generated from Smithy shape ``com.amazonaws.ram#ResourceShareAssociation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ram.types.boolean
    import aws_sdk_ram.types.date_time
    import aws_sdk_ram.types.resource_share_association_status
    import aws_sdk_ram.types.resource_share_association_type
    import aws_sdk_ram.types.string


class ResourceShareAssociation(TypedDict):
    resource_share_arn: NotRequired["aws_sdk_ram.types.string.String"]
    r"""<p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Name (ARN)</a> of the resource share.</p>"""
    resource_share_name: NotRequired["aws_sdk_ram.types.string.String"]
    """<p>The name of the resource share.</p>"""
    associated_entity: NotRequired["aws_sdk_ram.types.string.String"]
    r"""<p>The associated entity. This can be either of the following:</p> <ul> <li> <p>For a resource association, this is the <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Name (ARN)</a> of the resource.</p> </li> <li> <p>For principal associations, this is one of the following:</p> <ul> <li> <p>The ID of an Amazon Web Services account</p> </li> <li> <p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Name (ARN)</a> of an organization in Organizations</p> </li> <li> <p>The ARN of an organizational unit (OU) in Organizations</p> </li> <li> <p>The ARN of an IAM role</p> </li> <li> <p>The ARN of an IAM user</p> </li> </ul> </li> </ul>"""
    association_type: NotRequired[
        "aws_sdk_ram.types.resource_share_association_type.ResourceShareAssociationType"
    ]
    """<p>The type of entity included in this association.</p>"""
    status: NotRequired[
        "aws_sdk_ram.types.resource_share_association_status.ResourceShareAssociationStatus"
    ]
    """<p>The current status of the association.</p>"""
    status_message: NotRequired["aws_sdk_ram.types.string.String"]
    """<p>A message about the status of the association.</p>"""
    creation_time: NotRequired["aws_sdk_ram.types.date_time.DateTime"]
    """<p>The date and time when the association was created.</p>"""
    last_updated_time: NotRequired["aws_sdk_ram.types.date_time.DateTime"]
    """<p>The date and time when the association was last updated.</p>"""
    external: NotRequired["aws_sdk_ram.types.boolean.Boolean"]
    """<p>Indicates whether the principal belongs to the same organization in Organizations as the Amazon Web Services account that owns the resource share.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceShareAssociation) -> dict:
    out: dict = {}
    if "resource_share_arn" in value:
        out["resourceShareArn"] = value["resource_share_arn"]
    if "resource_share_name" in value:
        out["resourceShareName"] = value["resource_share_name"]
    if "associated_entity" in value:
        out["associatedEntity"] = value["associated_entity"]
    if "association_type" in value:
        import aws_sdk_ram.types.resource_share_association_type

        out["associationType"] = (
            aws_sdk_ram.types.resource_share_association_type.serialize_json(
                value["association_type"]
            )
        )
    if "status" in value:
        import aws_sdk_ram.types.resource_share_association_status

        out["status"] = (
            aws_sdk_ram.types.resource_share_association_status.serialize_json(
                value["status"]
            )
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
    if "external" in value:
        out["external"] = value["external"]
    return out


def deserialize_json(data: dict) -> ResourceShareAssociation:
    out: ResourceShareAssociation = {}  # type: ignore[typeddict-item]
    if "resourceShareArn" in data:
        out["resource_share_arn"] = data["resourceShareArn"]
    if "resourceShareName" in data:
        out["resource_share_name"] = data["resourceShareName"]
    if "associatedEntity" in data:
        out["associated_entity"] = data["associatedEntity"]
    if "associationType" in data:
        import aws_sdk_ram.types.resource_share_association_type

        out["association_type"] = (
            aws_sdk_ram.types.resource_share_association_type.deserialize_json(
                data["associationType"]
            )
        )
    if "status" in data:
        import aws_sdk_ram.types.resource_share_association_status

        out["status"] = (
            aws_sdk_ram.types.resource_share_association_status.deserialize_json(
                data["status"]
            )
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
    if "external" in data:
        out["external"] = data["external"]
    return out
