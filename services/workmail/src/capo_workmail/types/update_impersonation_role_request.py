"""Generated from Smithy shape ``com.amazonaws.workmail#UpdateImpersonationRoleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workmail.types.impersonation_role_description
    import capo_workmail.types.impersonation_role_id
    import capo_workmail.types.impersonation_role_name
    import capo_workmail.types.impersonation_role_type
    import capo_workmail.types.impersonation_rule_list
    import capo_workmail.types.organization_id


class UpdateImpersonationRoleRequest(TypedDict, closed=True):
    organization_id: "capo_workmail.types.organization_id.OrganizationId"
    """<p>The WorkMail organization that contains the impersonation role to update.</p>"""
    impersonation_role_id: (
        "capo_workmail.types.impersonation_role_id.ImpersonationRoleId"
    )
    """<p>The ID of the impersonation role to update.</p>"""
    name: "capo_workmail.types.impersonation_role_name.ImpersonationRoleName"
    """<p>The updated impersonation role name.</p>"""
    type: "capo_workmail.types.impersonation_role_type.ImpersonationRoleType"
    """<p>The updated impersonation role type.</p>"""
    description: NotRequired[
        "capo_workmail.types.impersonation_role_description.ImpersonationRoleDescription"
    ]
    """<p>The updated impersonation role description.</p>"""
    rules: "capo_workmail.types.impersonation_rule_list.ImpersonationRuleList"
    """<p>The updated list of rules.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateImpersonationRoleRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["ImpersonationRoleId"] = value["impersonation_role_id"]
    out["Name"] = value["name"]
    import capo_workmail.types.impersonation_role_type

    out["Type"] = capo_workmail.types.impersonation_role_type.serialize_aws_json_1_1(
        value["type"]
    )
    if "description" in value:
        out["Description"] = value["description"]
    import capo_workmail.types.impersonation_rule_list

    out["Rules"] = capo_workmail.types.impersonation_rule_list.serialize_aws_json_1_1(
        value["rules"]
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
        import capo_workmail.types.impersonation_role_type

        out["type"] = (
            capo_workmail.types.impersonation_role_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("UpdateImpersonationRoleRequest.type required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "Rules" in data:
        import capo_workmail.types.impersonation_rule_list

        out["rules"] = (
            capo_workmail.types.impersonation_rule_list.deserialize_aws_json_1_1(
                data["Rules"]
            )
        )
    else:
        raise DeserializationError("UpdateImpersonationRoleRequest.rules required")
    return out
