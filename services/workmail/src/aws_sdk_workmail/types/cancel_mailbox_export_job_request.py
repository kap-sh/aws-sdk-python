"""Generated from Smithy shape ``com.amazonaws.workmail#CancelMailboxExportJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workmail.types.idempotency_client_token
    import aws_sdk_workmail.types.mailbox_export_job_id
    import aws_sdk_workmail.types.organization_id


class CancelMailboxExportJobRequest(TypedDict):
    client_token: (
        "aws_sdk_workmail.types.idempotency_client_token.IdempotencyClientToken"
    )
    """<p>The idempotency token for the client request.</p>"""
    job_id: "aws_sdk_workmail.types.mailbox_export_job_id.MailboxExportJobId"
    """<p>The job ID.</p>"""
    organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId"
    """<p>The organization ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelMailboxExportJobRequest) -> dict:
    out: dict = {}
    out["ClientToken"] = value["client_token"]
    out["JobId"] = value["job_id"]
    out["OrganizationId"] = value["organization_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelMailboxExportJobRequest:
    out: CancelMailboxExportJobRequest = {}  # type: ignore[typeddict-item]
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    else:
        raise DeserializationError(
            "CancelMailboxExportJobRequest.client_token required"
        )
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    else:
        raise DeserializationError("CancelMailboxExportJobRequest.job_id required")
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError(
            "CancelMailboxExportJobRequest.organization_id required"
        )
    return out
