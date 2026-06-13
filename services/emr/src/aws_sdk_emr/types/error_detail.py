"""Generated from Smithy shape ``com.amazonaws.emr#ErrorDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.error_data
    import aws_sdk_emr.types.string


class ErrorDetail(TypedDict):
    error_code: NotRequired["aws_sdk_emr.types.string.String"]
    """<p>The name or code associated with the error.</p>"""
    error_data: NotRequired["aws_sdk_emr.types.error_data.ErrorData"]
    """<p>A list of key value pairs that provides contextual information about why an error occured.</p>"""
    error_message: NotRequired["aws_sdk_emr.types.string.String"]
    """<p>A message that describes the error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ErrorDetail) -> dict:
    out: dict = {}
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_data" in value:
        import aws_sdk_emr.types.error_data

        out["ErrorData"] = aws_sdk_emr.types.error_data.serialize_aws_json_1_1(
            value["error_data"]
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ErrorDetail:
    out: ErrorDetail = {}  # type: ignore[typeddict-item]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    if "ErrorData" in data:
        import aws_sdk_emr.types.error_data

        out["error_data"] = aws_sdk_emr.types.error_data.deserialize_aws_json_1_1(
            data["ErrorData"]
        )
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    return out
