"""Generated from Smithy shape ``com.amazonaws.resourcegroups#Group``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_resource_groups.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resource_groups.types.application_tag
    import aws_sdk_resource_groups.types.criticality
    import aws_sdk_resource_groups.types.description
    import aws_sdk_resource_groups.types.display_name
    import aws_sdk_resource_groups.types.group_arn_v2
    import aws_sdk_resource_groups.types.group_name
    import aws_sdk_resource_groups.types.owner


class Group(TypedDict):
    group_arn: "aws_sdk_resource_groups.types.group_arn_v2.GroupArnV2"
    """<p>The Amazon resource name (ARN) of the resource group.</p>"""
    name: "aws_sdk_resource_groups.types.group_name.GroupName"
    """<p>The name of the resource group.</p>"""
    description: NotRequired["aws_sdk_resource_groups.types.description.Description"]
    """<p>The description of the resource group.</p>"""
    criticality: NotRequired["aws_sdk_resource_groups.types.criticality.Criticality"]
    """<p>The critical rank of the application group on a scale of 1 to 10, with a rank of 1 being the most critical, and a rank of 10 being least critical.</p>"""
    owner: NotRequired["aws_sdk_resource_groups.types.owner.Owner"]
    """<p>A name, email address or other identifier for the person or group who is considered as the owner of this application group within your organization. </p>"""
    display_name: NotRequired["aws_sdk_resource_groups.types.display_name.DisplayName"]
    """<p>The name of the application group, which you can change at any time. </p>"""
    application_tag: NotRequired[
        "aws_sdk_resource_groups.types.application_tag.ApplicationTag"
    ]
    """<p>A tag that defines the application group membership. This tag is only supported for application groups. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Group) -> dict:
    out: dict = {}
    out["GroupArn"] = value["group_arn"]
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "criticality" in value:
        out["Criticality"] = value["criticality"]
    if "owner" in value:
        out["Owner"] = value["owner"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "application_tag" in value:
        import aws_sdk_resource_groups.types.application_tag

        out["ApplicationTag"] = (
            aws_sdk_resource_groups.types.application_tag.serialize_json(
                value["application_tag"]
            )
        )
    return out


def deserialize_json(data: dict) -> Group:
    out: Group = {}  # type: ignore[typeddict-item]
    if "GroupArn" in data:
        out["group_arn"] = data["GroupArn"]
    else:
        raise DeserializationError("Group.group_arn required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("Group.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "Criticality" in data:
        out["criticality"] = data["Criticality"]
    if "Owner" in data:
        out["owner"] = data["Owner"]
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    if "ApplicationTag" in data:
        import aws_sdk_resource_groups.types.application_tag

        out["application_tag"] = (
            aws_sdk_resource_groups.types.application_tag.deserialize_json(
                data["ApplicationTag"]
            )
        )
    return out
