"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#ProfileDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_rolesanywhere.types.attribute_mappings
    import capo_rolesanywhere.types.managed_policy_list
    import capo_rolesanywhere.types.profile_arn
    import capo_rolesanywhere.types.resource_name
    import capo_rolesanywhere.types.role_arn_list
    import capo_rolesanywhere.types.uuid


class ProfileDetail(TypedDict, closed=True):
    profile_id: NotRequired["capo_rolesanywhere.types.uuid.Uuid"]
    """<p>The unique identifier of the profile.</p>"""
    profile_arn: NotRequired["capo_rolesanywhere.types.profile_arn.ProfileArn"]
    """<p>The ARN of the profile.</p>"""
    name: NotRequired["capo_rolesanywhere.types.resource_name.ResourceName"]
    """<p>The name of the profile.</p>"""
    require_instance_properties: NotRequired["bool"]
    """<p>Unused, saved for future use. Will likely specify whether instance properties are required in temporary credential requests with this profile. </p>"""
    enabled: NotRequired["bool"]
    """<p>Indicates whether the profile is enabled.</p>"""
    created_by: NotRequired["str"]
    """<p>The Amazon Web Services account that created the profile.</p>"""
    session_policy: NotRequired["str"]
    """<p>A session policy that applies to the trust boundary of the vended session credentials. </p>"""
    role_arns: NotRequired["capo_rolesanywhere.types.role_arn_list.RoleArnList"]
    """<p>A list of IAM roles that this profile can assume in a temporary credential request.</p>"""
    managed_policy_arns: NotRequired[
        "capo_rolesanywhere.types.managed_policy_list.ManagedPolicyList"
    ]
    """<p>A list of managed policy ARNs that apply to the vended session credentials. </p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The ISO-8601 timestamp when the profile was created. </p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The ISO-8601 timestamp when the profile was last updated. </p>"""
    duration_seconds: NotRequired["int"]
    r"""<p> Used to determine how long sessions vended using this profile are valid for. See the <code>Expiration</code> section of the <a href=\"https://docs.aws.amazon.com/rolesanywhere/latest/userguide/authentication-create-session.html#credentials-object\">CreateSession API documentation</a> page for more details. In requests, if this value is not provided, the default value will be 3600. </p>"""
    accept_role_session_name: NotRequired["bool"]
    """<p>Used to determine if a custom role session name will be accepted in a temporary credential request.</p>"""
    attribute_mappings: NotRequired[
        "capo_rolesanywhere.types.attribute_mappings.AttributeMappings"
    ]
    """<p>A mapping applied to the authenticating end-entity certificate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProfileDetail) -> dict:
    out: dict = {}
    if "profile_id" in value:
        out["profileId"] = value["profile_id"]
    if "profile_arn" in value:
        out["profileArn"] = value["profile_arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "require_instance_properties" in value:
        out["requireInstanceProperties"] = value["require_instance_properties"]
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    if "session_policy" in value:
        out["sessionPolicy"] = value["session_policy"]
    if "role_arns" in value:
        import capo_rolesanywhere.types.role_arn_list

        out["roleArns"] = capo_rolesanywhere.types.role_arn_list.serialize_json(
            value["role_arns"]
        )
    if "managed_policy_arns" in value:
        import capo_rolesanywhere.types.managed_policy_list

        out["managedPolicyArns"] = (
            capo_rolesanywhere.types.managed_policy_list.serialize_json(
                value["managed_policy_arns"]
            )
        )
    if "created_at" in value:
        import capo_rolesanywhere.types._prelude.timestamp

        out["createdAt"] = capo_rolesanywhere.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_rolesanywhere.types._prelude.timestamp

        out["updatedAt"] = capo_rolesanywhere.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    if "duration_seconds" in value:
        out["durationSeconds"] = value["duration_seconds"]
    if "accept_role_session_name" in value:
        out["acceptRoleSessionName"] = value["accept_role_session_name"]
    if "attribute_mappings" in value:
        import capo_rolesanywhere.types.attribute_mappings

        out["attributeMappings"] = (
            capo_rolesanywhere.types.attribute_mappings.serialize_json(
                value["attribute_mappings"]
            )
        )
    return out


def deserialize_json(data: dict) -> ProfileDetail:
    out: ProfileDetail = {}  # type: ignore[typeddict-item]
    if "profileId" in data:
        out["profile_id"] = data["profileId"]
    if "profileArn" in data:
        out["profile_arn"] = data["profileArn"]
    if "name" in data:
        out["name"] = data["name"]
    if "requireInstanceProperties" in data:
        out["require_instance_properties"] = data["requireInstanceProperties"]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    if "sessionPolicy" in data:
        out["session_policy"] = data["sessionPolicy"]
    if "roleArns" in data:
        import capo_rolesanywhere.types.role_arn_list

        out["role_arns"] = capo_rolesanywhere.types.role_arn_list.deserialize_json(
            data["roleArns"]
        )
    if "managedPolicyArns" in data:
        import capo_rolesanywhere.types.managed_policy_list

        out["managed_policy_arns"] = (
            capo_rolesanywhere.types.managed_policy_list.deserialize_json(
                data["managedPolicyArns"]
            )
        )
    if "createdAt" in data:
        import capo_rolesanywhere.types._prelude.timestamp

        out["created_at"] = (
            capo_rolesanywhere.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    if "updatedAt" in data:
        import capo_rolesanywhere.types._prelude.timestamp

        out["updated_at"] = (
            capo_rolesanywhere.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    if "durationSeconds" in data:
        out["duration_seconds"] = data["durationSeconds"]
    if "acceptRoleSessionName" in data:
        out["accept_role_session_name"] = data["acceptRoleSessionName"]
    if "attributeMappings" in data:
        import capo_rolesanywhere.types.attribute_mappings

        out["attribute_mappings"] = (
            capo_rolesanywhere.types.attribute_mappings.deserialize_json(
                data["attributeMappings"]
            )
        )
    return out
