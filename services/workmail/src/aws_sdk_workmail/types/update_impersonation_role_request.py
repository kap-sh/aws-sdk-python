"""Generated from Smithy shape ``com.amazonaws.workmail#UpdateImpersonationRoleRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workmail.types.impersonation_role_description
    import aws_sdk_workmail.types.impersonation_role_id
    import aws_sdk_workmail.types.impersonation_role_name
    import aws_sdk_workmail.types.impersonation_role_type
    import aws_sdk_workmail.types.impersonation_rule_list
    import aws_sdk_workmail.types.organization_id


class UpdateImpersonationRoleRequest(TypedDict):
    organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId"
    """<p>The WorkMail organization that contains the impersonation role to update.</p>"""
    impersonation_role_id: (
        "aws_sdk_workmail.types.impersonation_role_id.ImpersonationRoleId"
    )
    """<p>The ID of the impersonation role to update.</p>"""
    name: "aws_sdk_workmail.types.impersonation_role_name.ImpersonationRoleName"
    """<p>The updated impersonation role name.</p>"""
    type: "aws_sdk_workmail.types.impersonation_role_type.ImpersonationRoleType"
    """<p>The updated impersonation role type.</p>"""
    description: NotRequired[
        "aws_sdk_workmail.types.impersonation_role_description.ImpersonationRoleDescription"
    ]
    """<p>The updated impersonation role description.</p>"""
    rules: "aws_sdk_workmail.types.impersonation_rule_list.ImpersonationRuleList"
    """<p>The updated list of rules.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateImpersonationRoleRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["ImpersonationRoleId"] = value["impersonation_role_id"]
    out["Name"] = value["name"]
    import aws_sdk_workmail.types.impersonation_role_type

    out["Type"] = aws_sdk_workmail.types.impersonation_role_type.serialize_aws_json_1_1(
        value["type"]
    )
    if "description" in value:
        out["Description"] = value["description"]
    import aws_sdk_workmail.types.impersonation_rule_list

    out["Rules"] = (
        aws_sdk_workmail.types.impersonation_rule_list.serialize_aws_json_1_1(
            value["rules"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateImpersonationRoleRequest:
    out: UpdateImpersonationRoleRequest = {}  # type: ignore[typeddict-item]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError(
            "UpdateImpersonationRoleRequest.organization_id required"
        )
    if "ImpersonationRoleId" in data:
        out["impersonation_role_id"] = data["ImpersonationRoleId"]
    else:
        raise DeserializationError(
            "UpdateImpersonationRoleRequest.impersonation_role_id required"
        )
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateImpersonationRoleRequest.name required")
    if "Type" in data:
        import aws_sdk_workmail.types.impersonation_role_type

        out["type"] = (
            aws_sdk_workmail.types.impersonation_role_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("UpdateImpersonationRoleRequest.type required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "Rules" in data:
        import aws_sdk_workmail.types.impersonation_rule_list

        out["rules"] = (
            aws_sdk_workmail.types.impersonation_rule_list.deserialize_aws_json_1_1(
                data["Rules"]
            )
        )
    else:
        raise DeserializationError("UpdateImpersonationRoleRequest.rules required")
    return out
