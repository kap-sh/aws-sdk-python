"""Generated from Smithy shape ``com.amazonaws.datasync#TaskExecutionFilesFailedDetail``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datasync.types.long


class TaskExecutionFilesFailedDetail(TypedDict):
    prepare: "aws_sdk_datasync.types.long.long"
    """<p>The number of files or objects that DataSync fails to prepare during your task execution.</p>"""
    transfer: "aws_sdk_datasync.types.long.long"
    """<p>The number of files or objects that DataSync fails to transfer during your task execution.</p>"""
    verify: "aws_sdk_datasync.types.long.long"
    """<p>The number of files or objects that DataSync fails to verify during your task execution.</p>"""
    delete: "aws_sdk_datasync.types.long.long"
    """<p>The number of files or objects that DataSync fails to delete during your task execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskExecutionFilesFailedDetail) -> dict:
    out: dict = {}
    out["Prepare"] = value.get("prepare", 0)
    out["Transfer"] = value.get("transfer", 0)
    out["Verify"] = value.get("verify", 0)
    out["Delete"] = value.get("delete", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> TaskExecutionFilesFailedDetail:
    out: TaskExecutionFilesFailedDetail = {}  # type: ignore[typeddict-item]
    if "Prepare" in data:
        out["prepare"] = data["Prepare"]
    else:
        out["prepare"] = 0
    if "Transfer" in data:
        out["transfer"] = data["Transfer"]
    else:
        out["transfer"] = 0
    if "Verify" in data:
        out["verify"] = data["Verify"]
    else:
        out["verify"] = 0
    if "Delete" in data:
        out["delete"] = data["Delete"]
    else:
        out["delete"] = 0
    return out
