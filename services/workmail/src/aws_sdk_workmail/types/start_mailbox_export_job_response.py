"""Generated from Smithy shape ``com.amazonaws.workmail#StartMailboxExportJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workmail.types.mailbox_export_job_id


class StartMailboxExportJobResponse(TypedDict):
    job_id: NotRequired[
        "aws_sdk_workmail.types.mailbox_export_job_id.MailboxExportJobId"
    ]
    """<p>The job ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartMailboxExportJobResponse) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartMailboxExportJobResponse:
    out: StartMailboxExportJobResponse = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    return out
