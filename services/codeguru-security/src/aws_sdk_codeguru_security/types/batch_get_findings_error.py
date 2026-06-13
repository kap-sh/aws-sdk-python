"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#BatchGetFindingsError``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codeguru_security.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codeguru_security.types.error_code
    import aws_sdk_codeguru_security.types.scan_name


class BatchGetFindingsError(TypedDict):
    scan_name: "aws_sdk_codeguru_security.types.scan_name.ScanName"
    """<p>The name of the scan that generated the finding.</p>"""
    finding_id: "str"
    """<p>The finding ID of the finding that was not fetched.</p>"""
    error_code: "aws_sdk_codeguru_security.types.error_code.ErrorCode"
    """<p>A code associated with the type of error.</p>"""
    message: "str"
    """<p>Describes the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetFindingsError) -> dict:
    out: dict = {}
    out["scanName"] = value["scan_name"]
    out["findingId"] = value["finding_id"]
    import aws_sdk_codeguru_security.types.error_code

    out["errorCode"] = aws_sdk_codeguru_security.types.error_code.serialize_json(
        value["error_code"]
    )
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BatchGetFindingsError:
    out: BatchGetFindingsError = {}  # type: ignore[typeddict-item]
    if "scanName" in data:
        out["scan_name"] = data["scanName"]
    else:
        raise DeserializationError("BatchGetFindingsError.scan_name required")
    if "findingId" in data:
        out["finding_id"] = data["findingId"]
    else:
        raise DeserializationError("BatchGetFindingsError.finding_id required")
    if "errorCode" in data:
        import aws_sdk_codeguru_security.types.error_code

        out["error_code"] = aws_sdk_codeguru_security.types.error_code.deserialize_json(
            data["errorCode"]
        )
    else:
        raise DeserializationError("BatchGetFindingsError.error_code required")
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("BatchGetFindingsError.message required")
    return out
