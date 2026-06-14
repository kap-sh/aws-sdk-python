"""Generated from Smithy shape ``com.amazonaws.connect#CreateSecurityProfileRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.allowed_access_control_tags
    import aws_sdk_connect.types.allowed_flow_modules
    import aws_sdk_connect.types.applications
    import aws_sdk_connect.types.create_security_profile_name
    import aws_sdk_connect.types.granular_access_control_configuration
    import aws_sdk_connect.types.hierarchy_group_id
    import aws_sdk_connect.types.hierarchy_restricted_resource_list
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.permissions_list
    import aws_sdk_connect.types.security_profile_description
    import aws_sdk_connect.types.tag_map
    import aws_sdk_connect.types.tag_restricted_resource_list


class CreateSecurityProfileRequest(TypedDict):
    security_profile_name: (
        "aws_sdk_connect.types.create_security_profile_name.CreateSecurityProfileName"
    )
    """<p>The name of the security profile.</p>"""
    description: NotRequired[
        "aws_sdk_connect.types.security_profile_description.SecurityProfileDescription"
    ]
    """<p>The description of the security profile.</p>"""
    permissions: NotRequired["aws_sdk_connect.types.permissions_list.PermissionsList"]
    r"""<p>Permissions assigned to the security profile. For a list of valid permissions, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/security-profile-list.html\">List of security profile permissions</a>. </p>"""
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    tags: NotRequired["aws_sdk_connect.types.tag_map.TagMap"]
    r"""<p>The tags used to organize, track, or control access for this resource. For example, { \"Tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>"""
    allowed_access_control_tags: NotRequired[
        "aws_sdk_connect.types.allowed_access_control_tags.AllowedAccessControlTags"
    ]
    """<p>The list of tags that a security profile uses to restrict access to resources in Connect Customer.</p>"""
    tag_restricted_resources: NotRequired[
        "aws_sdk_connect.types.tag_restricted_resource_list.TagRestrictedResourceList"
    ]
    r"""<p>The list of resources that a security profile applies tag restrictions to in Connect Customer. For a list of Connect Customer resources that you can tag, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/tagging.html\">Add tags to resources in Connect Customer</a> in the <i>Connect Customer Administrator Guide</i>. </p>"""
    applications: NotRequired["aws_sdk_connect.types.applications.Applications"]
    """<p>A list of third-party applications or MCP Servers that the security profile will give access to.</p>"""
    hierarchy_restricted_resources: NotRequired[
        "aws_sdk_connect.types.hierarchy_restricted_resource_list.HierarchyRestrictedResourceList"
    ]
    """<p>The list of resources that a security profile applies hierarchy restrictions to in Connect Customer. Following are acceptable ResourceNames: <code>User</code>.</p>"""
    allowed_access_control_hierarchy_group_id: NotRequired[
        "aws_sdk_connect.types.hierarchy_group_id.HierarchyGroupId"
    ]
    """<p>The identifier of the hierarchy group that a security profile uses to restrict access to resources in Connect Customer.</p>"""
    allowed_flow_modules: NotRequired[
        "aws_sdk_connect.types.allowed_flow_modules.AllowedFlowModules"
    ]
    """<p> A list of Flow Modules an AI Agent can invoke as a tool. </p>"""
    granular_access_control_configuration: NotRequired[
        "aws_sdk_connect.types.granular_access_control_configuration.GranularAccessControlConfiguration"
    ]
    """<p>The granular access control configuration for the security profile, including data table permissions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSecurityProfileRequest) -> dict:
    out: dict = {}
    out["SecurityProfileName"] = value["security_profile_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "permissions" in value:
        import aws_sdk_connect.types.permissions_list

        out["Permissions"] = aws_sdk_connect.types.permissions_list.serialize_json(
            value["permissions"]
        )
    if "tags" in value:
        import aws_sdk_connect.types.tag_map

        out["Tags"] = aws_sdk_connect.types.tag_map.serialize_json(value["tags"])
    if "allowed_access_control_tags" in value:
        import aws_sdk_connect.types.allowed_access_control_tags

        out["AllowedAccessControlTags"] = (
            aws_sdk_connect.types.allowed_access_control_tags.serialize_json(
                value["allowed_access_control_tags"]
            )
        )
    if "tag_restricted_resources" in value:
        import aws_sdk_connect.types.tag_restricted_resource_list

        out["TagRestrictedResources"] = (
            aws_sdk_connect.types.tag_restricted_resource_list.serialize_json(
                value["tag_restricted_resources"]
            )
        )
    if "applications" in value:
        import aws_sdk_connect.types.applications

        out["Applications"] = aws_sdk_connect.types.applications.serialize_json(
            value["applications"]
        )
    if "hierarchy_restricted_resources" in value:
        import aws_sdk_connect.types.hierarchy_restricted_resource_list

        out["HierarchyRestrictedResources"] = (
            aws_sdk_connect.types.hierarchy_restricted_resource_list.serialize_json(
                value["hierarchy_restricted_resources"]
            )
        )
    if "allowed_access_control_hierarchy_group_id" in value:
        out["AllowedAccessControlHierarchyGroupId"] = value[
            "allowed_access_control_hierarchy_group_id"
        ]
    if "allowed_flow_modules" in value:
        import aws_sdk_connect.types.allowed_flow_modules

        out["AllowedFlowModules"] = (
            aws_sdk_connect.types.allowed_flow_modules.serialize_json(
                value["allowed_flow_modules"]
            )
        )
    if "granular_access_control_configuration" in value:
        import aws_sdk_connect.types.granular_access_control_configuration

        out["GranularAccessControlConfiguration"] = (
            aws_sdk_connect.types.granular_access_control_configuration.serialize_json(
                value["granular_access_control_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateSecurityProfileRequest:
    out: CreateSecurityProfileRequest = {}  # type: ignore[typeddict-item]
    if "SecurityProfileName" in data:
        out["security_profile_name"] = data["SecurityProfileName"]
    else:
        raise DeserializationError(
            "CreateSecurityProfileRequest.security_profile_name required"
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "Permissions" in data:
        import aws_sdk_connect.types.permissions_list

        out["permissions"] = aws_sdk_connect.types.permissions_list.deserialize_json(
            data["Permissions"]
        )
    if "Tags" in data:
        import aws_sdk_connect.types.tag_map

        out["tags"] = aws_sdk_connect.types.tag_map.deserialize_json(data["Tags"])
    if "AllowedAccessControlTags" in data:
        import aws_sdk_connect.types.allowed_access_control_tags

        out["allowed_access_control_tags"] = (
            aws_sdk_connect.types.allowed_access_control_tags.deserialize_json(
                data["AllowedAccessControlTags"]
            )
        )
    if "TagRestrictedResources" in data:
        import aws_sdk_connect.types.tag_restricted_resource_list

        out["tag_restricted_resources"] = (
            aws_sdk_connect.types.tag_restricted_resource_list.deserialize_json(
                data["TagRestrictedResources"]
            )
        )
    if "Applications" in data:
        import aws_sdk_connect.types.applications

        out["applications"] = aws_sdk_connect.types.applications.deserialize_json(
            data["Applications"]
        )
    if "HierarchyRestrictedResources" in data:
        import aws_sdk_connect.types.hierarchy_restricted_resource_list

        out["hierarchy_restricted_resources"] = (
            aws_sdk_connect.types.hierarchy_restricted_resource_list.deserialize_json(
                data["HierarchyRestrictedResources"]
            )
        )
    if "AllowedAccessControlHierarchyGroupId" in data:
        out["allowed_access_control_hierarchy_group_id"] = data[
            "AllowedAccessControlHierarchyGroupId"
        ]
    if "AllowedFlowModules" in data:
        import aws_sdk_connect.types.allowed_flow_modules

        out["allowed_flow_modules"] = (
            aws_sdk_connect.types.allowed_flow_modules.deserialize_json(
                data["AllowedFlowModules"]
            )
        )
    if "GranularAccessControlConfiguration" in data:
        import aws_sdk_connect.types.granular_access_control_configuration

        out["granular_access_control_configuration"] = (
            aws_sdk_connect.types.granular_access_control_configuration.deserialize_json(
                data["GranularAccessControlConfiguration"]
            )
        )
    return out
