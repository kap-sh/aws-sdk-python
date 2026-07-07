"""Generated from Smithy shape ``com.amazonaws.backup#DescribeCopyJobOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_backup.types.copy_job


class DescribeCopyJobOutput(TypedDict, closed=True):
    copy_job: NotRequired["aws_sdk_backup.types.copy_job.CopyJob"]
    """<p>Contains detailed information about a copy job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeCopyJobOutput) -> dict:
    out: dict = {}
    if "copy_job" in value:
        import aws_sdk_backup.types.copy_job

        out["CopyJob"] = aws_sdk_backup.types.copy_job.serialize_json(value["copy_job"])
    return out


def deserialize_json(data: dict) -> DescribeCopyJobOutput:
    out: DescribeCopyJobOutput = {}  # type: ignore[typeddict-item]
    if "CopyJob" in data:
        import aws_sdk_backup.types.copy_job

        out["copy_job"] = aws_sdk_backup.types.copy_job.deserialize_json(
            data["CopyJob"]
        )
    return out
