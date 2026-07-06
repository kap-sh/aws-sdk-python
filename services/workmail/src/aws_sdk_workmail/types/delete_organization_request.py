"""Generated from Smithy shape ``com.amazonaws.workmail#DeleteOrganizationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workmail.types.boolean
    import aws_sdk_workmail.types.idempotency_client_token
    import aws_sdk_workmail.types.organization_id


class DeleteOrganizationRequest(TypedDict, closed=True):
    client_token: NotRequired[
        "aws_sdk_workmail.types.idempotency_client_token.IdempotencyClientToken"
    ]
    """<p>The idempotency token associated with the request.</p>"""
    organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId"
    """<p>The organization ID.</p>"""
    delete_directory: "aws_sdk_workmail.types.boolean.Boolean"
    """<p>If true, deletes the AWS Directory Service directory associated with the organization.</p>"""
    force_delete: "aws_sdk_workmail.types.boolean.Boolean"
    """<p>Deletes a WorkMail organization even if the organization has enabled users.</p>"""
    delete_identity_center_application: "aws_sdk_workmail.types.boolean.Boolean"
    """<p>Deletes IAM Identity Center application for WorkMail. This action does not affect authentication settings for any organization.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteOrganizationRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["OrganizationId"] = value["organization_id"]
    out["DeleteDirectory"] = value.get("delete_directory", False)
    out["ForceDelete"] = value.get("force_delete", False)
    out["DeleteIdentityCenterApplication"] = value.get(
        "delete_identity_center_application", False
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteOrganizationRequest:
    out: DeleteOrganizationRequest = {}  # type: ignore[typeddict-item]
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError("DeleteOrganizationRequest.organization_id required")
    if "DeleteDirectory" in data:
        out["delete_directory"] = data["DeleteDirectory"]
    else:
        out["delete_directory"] = False
    if "ForceDelete" in data:
        out["force_delete"] = data["ForceDelete"]
    else:
        out["force_delete"] = False
    if "DeleteIdentityCenterApplication" in data:
        out["delete_identity_center_application"] = data[
            "DeleteIdentityCenterApplication"
        ]
    else:
        out["delete_identity_center_application"] = False
    return out
