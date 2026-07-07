"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#ScanSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codeguru_security.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_codeguru_security.types.scan_name
    import aws_sdk_codeguru_security.types.scan_name_arn
    import aws_sdk_codeguru_security.types.scan_state
    import aws_sdk_codeguru_security.types.uuid


class ScanSummary(TypedDict, closed=True):
    scan_state: "aws_sdk_codeguru_security.types.scan_state.ScanState"
    """<p>The state of the scan. A scan can be <code>In Progress</code>, <code>Complete</code>, or <code>Failed</code>. </p>"""
    created_at: "datetime.datetime"
    """<p> The time when the scan was created. </p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The time the scan was last updated. A scan is updated when it is re-run.</p>"""
    scan_name: "aws_sdk_codeguru_security.types.scan_name.ScanName"
    """<p>The name of the scan. </p>"""
    run_id: "aws_sdk_codeguru_security.types.uuid.Uuid"
    """<p>The identifier for the scan run. </p>"""
    scan_name_arn: NotRequired[
        "aws_sdk_codeguru_security.types.scan_name_arn.ScanNameArn"
    ]
    """<p>The ARN for the scan name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScanSummary) -> dict:
    out: dict = {}
    import aws_sdk_codeguru_security.types.scan_state

    out["scanState"] = aws_sdk_codeguru_security.types.scan_state.serialize_json(
        value["scan_state"]
    )
    import aws_sdk_codeguru_security.types._prelude.timestamp

    out["createdAt"] = (
        aws_sdk_codeguru_security.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    )
    if "updated_at" in value:
        import aws_sdk_codeguru_security.types._prelude.timestamp

        out["updatedAt"] = (
            aws_sdk_codeguru_security.types._prelude.timestamp.serialize_json(
                value["updated_at"]
            )
        )
    out["scanName"] = value["scan_name"]
    out["runId"] = value["run_id"]
    if "scan_name_arn" in value:
        out["scanNameArn"] = value["scan_name_arn"]
    return out


def deserialize_json(data: dict) -> ScanSummary:
    out: ScanSummary = {}  # type: ignore[typeddict-item]
    if "scanState" in data:
        import aws_sdk_codeguru_security.types.scan_state

        out["scan_state"] = aws_sdk_codeguru_security.types.scan_state.deserialize_json(
            data["scanState"]
        )
    else:
        raise DeserializationError("ScanSummary.scan_state required")
    if "createdAt" in data:
        import aws_sdk_codeguru_security.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_codeguru_security.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("ScanSummary.created_at required")
    if "updatedAt" in data:
        import aws_sdk_codeguru_security.types._prelude.timestamp

        out["updated_at"] = (
            aws_sdk_codeguru_security.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    if "scanName" in data:
        out["scan_name"] = data["scanName"]
    else:
        raise DeserializationError("ScanSummary.scan_name required")
    if "runId" in data:
        out["run_id"] = data["runId"]
    else:
        raise DeserializationError("ScanSummary.run_id required")
    if "scanNameArn" in data:
        out["scan_name_arn"] = data["scanNameArn"]
    return out
