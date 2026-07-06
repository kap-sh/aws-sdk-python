"""Generated from Smithy shape ``com.amazonaws.datazone#CreateGroupProfileOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.group_profile_id
    import aws_sdk_datazone.types.group_profile_name
    import aws_sdk_datazone.types.group_profile_status


class CreateGroupProfileOutput(TypedDict, closed=True):
    domain_id: NotRequired["aws_sdk_datazone.types.domain_id.DomainId"]
    """<p>The identifier of the Amazon DataZone domain in which the group profile is created.</p>"""
    id: NotRequired["aws_sdk_datazone.types.group_profile_id.GroupProfileId"]
    """<p>The identifier of the group profile.</p>"""
    status: NotRequired[
        "aws_sdk_datazone.types.group_profile_status.GroupProfileStatus"
    ]
    """<p>The status of the group profile.</p>"""
    group_name: NotRequired[
        "aws_sdk_datazone.types.group_profile_name.GroupProfileName"
    ]
    """<p>The name of the group for which group profile is created.</p>"""
    role_principal_arn: NotRequired["str"]
    """<p>The ARN of the IAM role principal. This role is associated with the group profile.</p>"""
    role_principal_id: NotRequired["str"]
    """<p>The unique identifier of the IAM role principal. This principal is associated with the group profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateGroupProfileOutput) -> dict:
    out: dict = {}
    if "domain_id" in value:
        out["domainId"] = value["domain_id"]
    if "id" in value:
        out["id"] = value["id"]
    if "status" in value:
        import aws_sdk_datazone.types.group_profile_status

        out["status"] = aws_sdk_datazone.types.group_profile_status.serialize_json(
            value["status"]
        )
    if "group_name" in value:
        out["groupName"] = value["group_name"]
    if "role_principal_arn" in value:
        out["rolePrincipalArn"] = value["role_principal_arn"]
    if "role_principal_id" in value:
        out["rolePrincipalId"] = value["role_principal_id"]
    return out


def deserialize_json(data: dict) -> CreateGroupProfileOutput:
    out: CreateGroupProfileOutput = {}  # type: ignore[typeddict-item]
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    if "id" in data:
        out["id"] = data["id"]
    if "status" in data:
        import aws_sdk_datazone.types.group_profile_status

        out["status"] = aws_sdk_datazone.types.group_profile_status.deserialize_json(
            data["status"]
        )
    if "groupName" in data:
        out["group_name"] = data["groupName"]
    if "rolePrincipalArn" in data:
        out["role_principal_arn"] = data["rolePrincipalArn"]
    if "rolePrincipalId" in data:
        out["role_principal_id"] = data["rolePrincipalId"]
    return out
