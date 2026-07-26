"""Generated from Smithy shape ``com.amazonaws.workmail#Jobs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workmail.types.mailbox_export_job

Jobs: TypeAlias = list["capo_workmail.types.mailbox_export_job.MailboxExportJob"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Jobs) -> list:
    import capo_workmail.types.mailbox_export_job

    out: list = []
    for item in value:
        out.append(capo_workmail.types.mailbox_export_job.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Jobs:
    import capo_workmail.types.mailbox_export_job

    out: Jobs = []
    for item in data:
        out.append(
            capo_workmail.types.mailbox_export_job.deserialize_aws_json_1_1(item)
        )
    return out
