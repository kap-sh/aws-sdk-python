"""Generated from Smithy shape ``com.amazonaws.backup#StartScanJobOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_backup.errors import DeserializationError

if TYPE_CHECKING:
    import datetime


class StartScanJobOutput(TypedDict, closed=True):
    creation_date: "datetime.datetime"
    """<p>The date and time that a backup job is created, in Unix format and Coordinated Universal Time (UTC). The value of <code>CreationDate</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""
    scan_job_id: "str"
    """<p>Uniquely identifies a request to Backup to back up a resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartScanJobOutput) -> dict:
    out: dict = {}
    import aws_sdk_backup.types._prelude.timestamp

    out["CreationDate"] = aws_sdk_backup.types._prelude.timestamp.serialize_json(
        value["creation_date"]
    )
    out["ScanJobId"] = value["scan_job_id"]
    return out


def deserialize_json(data: dict) -> StartScanJobOutput:
    out: StartScanJobOutput = {}  # type: ignore[typeddict-item]
    if "CreationDate" in data:
        import aws_sdk_backup.types._prelude.timestamp

        out["creation_date"] = aws_sdk_backup.types._prelude.timestamp.deserialize_json(
            data["CreationDate"]
        )
    else:
        raise DeserializationError("StartScanJobOutput.creation_date required")
    if "ScanJobId" in data:
        out["scan_job_id"] = data["ScanJobId"]
    else:
        raise DeserializationError("StartScanJobOutput.scan_job_id required")
    return out
