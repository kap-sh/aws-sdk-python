"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#BatchDescribeErrorDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.batch_describe_error_code_string
    import capo_marketplace_catalog.types.batch_describe_error_message_content


class BatchDescribeErrorDetail(TypedDict, closed=True):
    error_code: NotRequired[
        "capo_marketplace_catalog.types.batch_describe_error_code_string.BatchDescribeErrorCodeString"
    ]
    """<p>The error code returned.</p>"""
    error_message: NotRequired[
        "capo_marketplace_catalog.types.batch_describe_error_message_content.BatchDescribeErrorMessageContent"
    ]
    """<p>The error message returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDescribeErrorDetail) -> dict:
    out: dict = {}
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> BatchDescribeErrorDetail:
    out: BatchDescribeErrorDetail = {}  # type: ignore[typeddict-item]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    return out
