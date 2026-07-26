"""Generated from Smithy shape ``com.amazonaws.connect#SecurityProfile``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.allowed_access_control_tags
    import capo_connect.types.arn
    import capo_connect.types.granular_access_control_configuration
    import capo_connect.types.hierarchy_group_id
    import capo_connect.types.hierarchy_restricted_resource_list
    import capo_connect.types.instance_id
    import capo_connect.types.region_name
    import capo_connect.types.security_profile_description
    import capo_connect.types.security_profile_id
    import capo_connect.types.security_profile_name
    import capo_connect.types.tag_map
    import capo_connect.types.tag_restricted_resource_list
    import capo_connect.types.timestamp


class SecurityProfile(TypedDict, closed=True):
    id: NotRequired["capo_connect.types.security_profile_id.SecurityProfileId"]
    """<p>The identifier for the security profile.</p>"""
    organization_resource_id: NotRequired["capo_connect.types.instance_id.InstanceId"]
    """<p>The organization resource identifier for the security profile.</p>"""
    arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) for the security profile.</p>"""
    security_profile_name: NotRequired[
        "capo_connect.types.security_profile_name.SecurityProfileName"
    ]
    """<p>The name for the security profile.</p>"""
    description: NotRequired[
        "capo_connect.types.security_profile_description.SecurityProfileDescription"
    ]
    """<p>The description of the security profile.</p>"""
    tags: NotRequired["capo_connect.types.tag_map.TagMap"]
    r"""<p>The tags used to organize, track, or control access for this resource. For example, { \"Tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>"""
    allowed_access_control_tags: NotRequired[
        "capo_connect.types.allowed_access_control_tags.AllowedAccessControlTags"
    ]
    """<p>The list of tags that a security profile uses to restrict access to resources in Connect Customer.</p>"""
    tag_restricted_resources: NotRequired[
        "capo_connect.types.tag_restricted_resource_list.TagRestrictedResourceList"
    ]
    """<p>The list of resources that a security profile applies tag restrictions to in Connect Customer.</p>"""
    last_modified_time: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when this resource was last modified.</p>"""
    last_modified_region: NotRequired["capo_connect.types.region_name.RegionName"]
    """<p>The Amazon Web Services Region where this resource was last modified.</p>"""
    hierarchy_restricted_resources: NotRequired[
        "capo_connect.types.hierarchy_restricted_resource_list.HierarchyRestrictedResourceList"
    ]
    """<p>The list of resources that a security profile applies hierarchy restrictions to in Connect Customer. Following are acceptable ResourceNames: <code>User</code>.</p>"""
    allowed_access_control_hierarchy_group_id: NotRequired[
        "capo_connect.types.hierarchy_group_id.HierarchyGroupId"
    ]
    """<p>The identifier of the hierarchy group that a security profile uses to restrict access to resources in Connect Customer.</p>"""
    granular_access_control_configuration: NotRequired[
        "capo_connect.types.granular_access_control_configuration.GranularAccessControlConfiguration"
    ]
    """<p>The granular access control configuration for the security profile, including data table permissions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SecurityProfile) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "organization_resource_id" in value:
        out["OrganizationResourceId"] = value["organization_resource_id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "security_profile_name" in value:
        out["SecurityProfileName"] = value["security_profile_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import capo_connect.types.tag_map

        out["Tags"] = capo_connect.types.tag_map.serialize_json(value["tags"])
    if "allowed_access_control_tags" in value:
        import capo_connect.types.allowed_access_control_tags

        out["AllowedAccessControlTags"] = (
            capo_connect.types.allowed_access_control_tags.serialize_json(
                value["allowed_access_control_tags"]
            )
        )
    if "tag_restricted_resources" in value:
        import capo_connect.types.tag_restricted_resource_list

        out["TagRestrictedResources"] = (
            capo_connect.types.tag_restricted_resource_list.serialize_json(
                value["tag_restricted_resources"]
            )
        )
    if "last_modified_time" in value:
        import capo_connect.types.timestamp

        out["LastModifiedTime"] = capo_connect.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    if "last_modified_region" in value:
        out["LastModifiedRegion"] = value["last_modified_region"]
    if "hierarchy_restricted_resources" in value:
        import capo_connect.types.hierarchy_restricted_resource_list

        out["HierarchyRestrictedResources"] = (
            capo_connect.types.hierarchy_restricted_resource_list.serialize_json(
                value["hierarchy_restricted_resources"]
            )
        )
    if "allowed_access_control_hierarchy_group_id" in value:
        out["AllowedAccessControlHierarchyGroupId"] = value[
            "allowed_access_control_hierarchy_group_id"
        ]
    if "granular_access_control_configuration" in value:
        import capo_connect.types.granular_access_control_configuration

        out["GranularAccessControlConfiguration"] = (
            capo_connect.types.granular_access_control_configuration.serialize_json(
                value["granular_access_control_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> SecurityProfile:
    out: SecurityProfile = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "OrganizationResourceId" in data:
        out["organization_resource_id"] = data["OrganizationResourceId"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "SecurityProfileName" in data:
        out["security_profile_name"] = data["SecurityProfileName"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Tags" in data:
        import capo_connect.types.tag_map

        out["tags"] = capo_connect.types.tag_map.deserialize_json(data["Tags"])
    if "AllowedAccessControlTags" in data:
        import capo_connect.types.allowed_access_control_tags

        out["allowed_access_control_tags"] = (
            capo_connect.types.allowed_access_control_tags.deserialize_json(
                data["AllowedAccessControlTags"]
            )
        )
    if "TagRestrictedResources" in data:
        import capo_connect.types.tag_restricted_resource_list

        out["tag_restricted_resources"] = (
            capo_connect.types.tag_restricted_resource_list.deserialize_json(
                data["TagRestrictedResources"]
            )
        )
    if "LastModifiedTime" in data:
        import capo_connect.types.timestamp

        out["last_modified_time"] = capo_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    if "LastModifiedRegion" in data:
        out["last_modified_region"] = data["LastModifiedRegion"]
    if "HierarchyRestrictedResources" in data:
        import capo_connect.types.hierarchy_restricted_resource_list

        out["hierarchy_restricted_resources"] = (
            capo_connect.types.hierarchy_restricted_resource_list.deserialize_json(
                data["HierarchyRestrictedResources"]
            )
        )
    if "AllowedAccessControlHierarchyGroupId" in data:
        out["allowed_access_control_hierarchy_group_id"] = data[
            "AllowedAccessControlHierarchyGroupId"
        ]
    if "GranularAccessControlConfiguration" in data:
        import capo_connect.types.granular_access_control_configuration

        out["granular_access_control_configuration"] = (
            capo_connect.types.granular_access_control_configuration.deserialize_json(
                data["GranularAccessControlConfiguration"]
            )
        )
    return out
