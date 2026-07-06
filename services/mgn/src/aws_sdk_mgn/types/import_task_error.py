"""Generated from Smithy shape ``com.amazonaws.mgn#ImportTaskError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mgn.types.import_error_data
    import aws_sdk_mgn.types.import_error_type
    import aws_sdk_mgn.types.iso8601_datetime_string


class ImportTaskError(TypedDict, closed=True):
    error_date_time: NotRequired[
        "aws_sdk_mgn.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>Import task error datetime.</p>"""
    error_type: NotRequired["aws_sdk_mgn.types.import_error_type.ImportErrorType"]
    """<p>Import task error type.</p>"""
    error_data: NotRequired["aws_sdk_mgn.types.import_error_data.ImportErrorData"]
    """<p>Import task error data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportTaskError) -> dict:
    out: dict = {}
    if "error_date_time" in value:
        out["errorDateTime"] = value["error_date_time"]
    if "error_type" in value:
        out["errorType"] = value["error_type"]
    if "error_data" in value:
        import aws_sdk_mgn.types.import_error_data

        out["errorData"] = aws_sdk_mgn.types.import_error_data.serialize_json(
            value["error_data"]
        )
    return out


def deserialize_json(data: dict) -> ImportTaskError:
    out: ImportTaskError = {}  # type: ignore[typeddict-item]
    if "errorDateTime" in data:
        out["error_date_time"] = data["errorDateTime"]
    if "errorType" in data:
        out["error_type"] = data["errorType"]
    if "errorData" in data:
        import aws_sdk_mgn.types.import_error_data

        out["error_data"] = aws_sdk_mgn.types.import_error_data.deserialize_json(
            data["errorData"]
        )
    return out
