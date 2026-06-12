"""Generated from Smithy shape ``com.amazonaws.workmail#DescribeMailboxExportJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workmail.types.mailbox_export_job_id
    import aws_sdk_workmail.types.organization_id


class DescribeMailboxExportJobRequest(TypedDict):
    job_id: "aws_sdk_workmail.types.mailbox_export_job_id.MailboxExportJobId"
    """<p>The mailbox export job ID.</p>"""
    organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId"
    """<p>The organization ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeMailboxExportJobRequest) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    out["OrganizationId"] = value["organization_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeMailboxExportJobRequest:
    out: DescribeMailboxExportJobRequest = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    else:
        raise DeserializationError("DescribeMailboxExportJobRequest.job_id required")
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError(
            "DescribeMailboxExportJobRequest.organization_id required"
        )
    return out
