"""Generated from Smithy shape ``com.amazonaws.datazone#UpdateGroupProfileOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.domain_id
    import capo_datazone.types.group_profile_id
    import capo_datazone.types.group_profile_name
    import capo_datazone.types.group_profile_status


class UpdateGroupProfileOutput(TypedDict, closed=True):
    domain_id: NotRequired["capo_datazone.types.domain_id.DomainId"]
    """<p>The identifier of the Amazon DataZone domain in which a group profile is updated.</p>"""
    id: NotRequired["capo_datazone.types.group_profile_id.GroupProfileId"]
    """<p>The identifier of the group profile that is updated.</p>"""
    status: NotRequired["capo_datazone.types.group_profile_status.GroupProfileStatus"]
    """<p>The status of the group profile that is updated.</p>"""
    group_name: NotRequired["capo_datazone.types.group_profile_name.GroupProfileName"]
    """<p>The name of the group profile that is updated.</p>"""
    role_principal_arn: NotRequired["str"]
    """<p>The ARN of the IAM role principal. This role is associated with the updated group profile.</p>"""
    role_principal_id: NotRequired["str"]
    """<p>The unique identifier of the IAM role principal. This principal is associated with the updated group profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGroupProfileOutput) -> dict:
    out: dict = {}
    if "domain_id" in value:
        out["domainId"] = value["domain_id"]
    if "id" in value:
        out["id"] = value["id"]
    if "status" in value:
        import capo_datazone.types.group_profile_status

        out["status"] = capo_datazone.types.group_profile_status.serialize_json(
            value["status"]
        )
    if "group_name" in value:
        out["groupName"] = value["group_name"]
    if "role_principal_arn" in value:
        out["rolePrincipalArn"] = value["role_principal_arn"]
    if "role_principal_id" in value:
        out["rolePrincipalId"] = value["role_principal_id"]
    return out


def deserialize_json(data: dict) -> UpdateGroupProfileOutput:
    out: UpdateGroupProfileOutput = {}  # type: ignore[typeddict-item]
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    if "id" in data:
        out["id"] = data["id"]
    if "status" in data:
        import capo_datazone.types.group_profile_status

        out["status"] = capo_datazone.types.group_profile_status.deserialize_json(
            data["status"]
        )
    if "groupName" in data:
        out["group_name"] = data["groupName"]
    if "rolePrincipalArn" in data:
        out["role_principal_arn"] = data["rolePrincipalArn"]
    if "rolePrincipalId" in data:
        out["role_principal_id"] = data["rolePrincipalId"]
    return out
