"""Generated from Smithy shape ``com.amazonaws.backup#ScanResultInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_backup.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_backup.types.scan_result_status


class ScanResultInfo(TypedDict, closed=True):
    scan_result_status: "aws_sdk_backup.types.scan_result_status.ScanResultStatus"
    """<p>The status of the scan results.</p> <p>Valid values: <code>THREATS_FOUND</code> | <code>NO_THREATS_FOUND</code> | <code>UNKNOWN</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScanResultInfo) -> dict:
    out: dict = {}
    import aws_sdk_backup.types.scan_result_status

    out["ScanResultStatus"] = aws_sdk_backup.types.scan_result_status.serialize_json(
        value["scan_result_status"]
    )
    return out


def deserialize_json(data: dict) -> ScanResultInfo:
    out: ScanResultInfo = {}  # type: ignore[typeddict-item]
    if "ScanResultStatus" in data:
        import aws_sdk_backup.types.scan_result_status

        out["scan_result_status"] = (
            aws_sdk_backup.types.scan_result_status.deserialize_json(
                data["ScanResultStatus"]
            )
        )
    else:
        raise DeserializationError("ScanResultInfo.scan_result_status required")
    return out
