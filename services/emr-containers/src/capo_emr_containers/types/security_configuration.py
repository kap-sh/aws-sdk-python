"""Generated from Smithy shape ``com.amazonaws.emrcontainers#SecurityConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_containers.types.date
    import capo_emr_containers.types.request_identity_user_arn
    import capo_emr_containers.types.resource_id_string
    import capo_emr_containers.types.resource_name_string
    import capo_emr_containers.types.security_configuration_arn
    import capo_emr_containers.types.security_configuration_data
    import capo_emr_containers.types.tag_map


class SecurityConfiguration(TypedDict, closed=True):
    id: NotRequired["capo_emr_containers.types.resource_id_string.ResourceIdString"]
    """<p>The ID of the security configuration.</p>"""
    name: NotRequired[
        "capo_emr_containers.types.resource_name_string.ResourceNameString"
    ]
    """<p>The name of the security configuration.</p>"""
    arn: NotRequired[
        "capo_emr_containers.types.security_configuration_arn.SecurityConfigurationArn"
    ]
    """<p>The ARN (Amazon Resource Name) of the security configuration.</p>"""
    created_at: NotRequired["capo_emr_containers.types.date.Date"]
    """<p>The date and time that the job run was created.</p>"""
    created_by: NotRequired[
        "capo_emr_containers.types.request_identity_user_arn.RequestIdentityUserArn"
    ]
    """<p>The user who created the job run.</p>"""
    security_configuration_data: NotRequired[
        "capo_emr_containers.types.security_configuration_data.SecurityConfigurationData"
    ]
    """<p>Security configuration inputs for the request.</p>"""
    tags: NotRequired["capo_emr_containers.types.tag_map.TagMap"]
    """<p>The tags to assign to the security configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SecurityConfiguration) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "created_at" in value:
        import capo_emr_containers.types.date

        out["createdAt"] = capo_emr_containers.types.date.serialize_json(
            value["created_at"]
        )
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    if "security_configuration_data" in value:
        import capo_emr_containers.types.security_configuration_data

        out["securityConfigurationData"] = (
            capo_emr_containers.types.security_configuration_data.serialize_json(
                value["security_configuration_data"]
            )
        )
    if "tags" in value:
        import capo_emr_containers.types.tag_map

        out["tags"] = capo_emr_containers.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> SecurityConfiguration:
    out: SecurityConfiguration = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "createdAt" in data:
        import capo_emr_containers.types.date

        out["created_at"] = capo_emr_containers.types.date.deserialize_json(
            data["createdAt"]
        )
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    if "securityConfigurationData" in data:
        import capo_emr_containers.types.security_configuration_data

        out["security_configuration_data"] = (
            capo_emr_containers.types.security_configuration_data.deserialize_json(
                data["securityConfigurationData"]
            )
        )
    if "tags" in data:
        import capo_emr_containers.types.tag_map

        out["tags"] = capo_emr_containers.types.tag_map.deserialize_json(data["tags"])
    return out
