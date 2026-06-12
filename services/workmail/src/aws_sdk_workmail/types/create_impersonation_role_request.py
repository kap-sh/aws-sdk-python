"""Generated from Smithy shape ``com.amazonaws.workmail#CreateImpersonationRoleRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workmail.types.idempotency_client_token
    import aws_sdk_workmail.types.impersonation_role_description
    import aws_sdk_workmail.types.impersonation_role_name
    import aws_sdk_workmail.types.impersonation_role_type
    import aws_sdk_workmail.types.impersonation_rule_list
    import aws_sdk_workmail.types.organization_id


class CreateImpersonationRoleRequest(TypedDict):
    client_token: NotRequired[
        "aws_sdk_workmail.types.idempotency_client_token.IdempotencyClientToken"
    ]
    """<p>The idempotency token for the client request.</p>"""
    organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId"
    """<p>The WorkMail organization to create the new impersonation role within.</p>"""
    name: "aws_sdk_workmail.types.impersonation_role_name.ImpersonationRoleName"
    """<p>The name of the new impersonation role.</p>"""
    type: "aws_sdk_workmail.types.impersonation_role_type.ImpersonationRoleType"
    """<p>The impersonation role's type. The available impersonation role types are <code>READ_ONLY</code> or <code>FULL_ACCESS</code>.</p>"""
    description: NotRequired[
        "aws_sdk_workmail.types.impersonation_role_description.ImpersonationRoleDescription"
    ]
    """<p>The description of the new impersonation role.</p>"""
    rules: "aws_sdk_workmail.types.impersonation_rule_list.ImpersonationRuleList"
    """<p>The list of rules for the impersonation role.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateImpersonationRoleRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["OrganizationId"] = value["organization_id"]
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


def deserialize_aws_json_1_1(data: dict) -> CreateImpersonationRoleRequest:
    out: CreateImpersonationRoleRequest = {}  # type: ignore[typeddict-item]
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError(
            "CreateImpersonationRoleRequest.organization_id required"
        )
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateImpersonationRoleRequest.name required")
    if "Type" in data:
        import aws_sdk_workmail.types.impersonation_role_type

        out["type"] = (
            aws_sdk_workmail.types.impersonation_role_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("CreateImpersonationRoleRequest.type required")
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
        raise DeserializationError("CreateImpersonationRoleRequest.rules required")
    return out
