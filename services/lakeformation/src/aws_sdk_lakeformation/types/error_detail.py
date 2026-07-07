"""Generated from Smithy shape ``com.amazonaws.lakeformation#ErrorDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.description_string
    import aws_sdk_lakeformation.types.name_string


class ErrorDetail(TypedDict, closed=True):
    error_code: NotRequired["aws_sdk_lakeformation.types.name_string.NameString"]
    """<p>The code associated with this error.</p>"""
    error_message: NotRequired[
        "aws_sdk_lakeformation.types.description_string.DescriptionString"
    ]
    """<p>A message describing the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ErrorDetail) -> dict:
    out: dict = {}
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> ErrorDetail:
    out: ErrorDetail = {}  # type: ignore[typeddict-item]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    return out
