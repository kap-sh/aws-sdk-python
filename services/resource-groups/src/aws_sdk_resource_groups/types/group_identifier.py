"""Generated from Smithy shape ``com.amazonaws.resourcegroups#GroupIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_resource_groups.types.criticality
    import aws_sdk_resource_groups.types.description
    import aws_sdk_resource_groups.types.display_name
    import aws_sdk_resource_groups.types.group_arn
    import aws_sdk_resource_groups.types.group_name
    import aws_sdk_resource_groups.types.owner


class GroupIdentifier(TypedDict, closed=True):
    group_name: NotRequired["aws_sdk_resource_groups.types.group_name.GroupName"]
    """<p>The name of the resource group.</p>"""
    group_arn: NotRequired["aws_sdk_resource_groups.types.group_arn.GroupArn"]
    """<p>The Amazon resource name (ARN) of the resource group.</p>"""
    description: NotRequired["aws_sdk_resource_groups.types.description.Description"]
    """<p>The description of the application group. </p>"""
    criticality: NotRequired["aws_sdk_resource_groups.types.criticality.Criticality"]
    """<p>The critical rank of the application group on a scale of 1 to 10, with a rank of 1 being the most critical, and a rank of 10 being least critical.</p>"""
    owner: NotRequired["aws_sdk_resource_groups.types.owner.Owner"]
    """<p>A name, email address or other identifier for the person or group who is considered as the owner of this group within your organization. </p>"""
    display_name: NotRequired["aws_sdk_resource_groups.types.display_name.DisplayName"]
    """<p>The name of the application group, which you can change at any time. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GroupIdentifier) -> dict:
    out: dict = {}
    if "group_name" in value:
        out["GroupName"] = value["group_name"]
    if "group_arn" in value:
        out["GroupArn"] = value["group_arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "criticality" in value:
        out["Criticality"] = value["criticality"]
    if "owner" in value:
        out["Owner"] = value["owner"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    return out


def deserialize_json(data: dict) -> GroupIdentifier:
    out: GroupIdentifier = {}  # type: ignore[typeddict-item]
    if "GroupName" in data:
        out["group_name"] = data["GroupName"]
    if "GroupArn" in data:
        out["group_arn"] = data["GroupArn"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Criticality" in data:
        out["criticality"] = data["Criticality"]
    if "Owner" in data:
        out["owner"] = data["Owner"]
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    return out
