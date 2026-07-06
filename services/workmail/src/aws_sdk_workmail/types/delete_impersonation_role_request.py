"""Generated from Smithy shape ``com.amazonaws.workmail#DeleteImpersonationRoleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workmail.types.impersonation_role_id
    import aws_sdk_workmail.types.organization_id


class DeleteImpersonationRoleRequest(TypedDict, closed=True):
    organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId"
    """<p>The WorkMail organization from which to delete the impersonation role.</p>"""
    impersonation_role_id: (
        "aws_sdk_workmail.types.impersonation_role_id.ImpersonationRoleId"
    )
    """<p>The ID of the impersonation role to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteImpersonationRoleRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["ImpersonationRoleId"] = value["impersonation_role_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteImpersonationRoleRequest:
    out: DeleteImpersonationRoleRequest = {}  # type: ignore[typeddict-item]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError(
            "DeleteImpersonationRoleRequest.organization_id required"
        )
    if "ImpersonationRoleId" in data:
        out["impersonation_role_id"] = data["ImpersonationRoleId"]
    else:
        raise DeserializationError(
            "DeleteImpersonationRoleRequest.impersonation_role_id required"
        )
    return out
