"""Generated from Smithy shape ``com.amazonaws.comprehend#ErrorsListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.integer
    import aws_sdk_comprehend.types.page_based_error_code
    import aws_sdk_comprehend.types.string


class ErrorsListItem(TypedDict, closed=True):
    page: NotRequired["aws_sdk_comprehend.types.integer.Integer"]
    """<p>Page number where the error occurred.</p>"""
    error_code: NotRequired[
        "aws_sdk_comprehend.types.page_based_error_code.PageBasedErrorCode"
    ]
    """<p>Error code for the cause of the error.</p>"""
    error_message: NotRequired["aws_sdk_comprehend.types.string.String"]
    """<p>Text message explaining the reason for the error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ErrorsListItem) -> dict:
    out: dict = {}
    if "page" in value:
        out["Page"] = value["page"]
    if "error_code" in value:
        import aws_sdk_comprehend.types.page_based_error_code

        out["ErrorCode"] = (
            aws_sdk_comprehend.types.page_based_error_code.serialize_aws_json_1_1(
                value["error_code"]
            )
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ErrorsListItem:
    out: ErrorsListItem = {}  # type: ignore[typeddict-item]
    if "Page" in data:
        out["page"] = data["Page"]
    if "ErrorCode" in data:
        import aws_sdk_comprehend.types.page_based_error_code

        out["error_code"] = (
            aws_sdk_comprehend.types.page_based_error_code.deserialize_aws_json_1_1(
                data["ErrorCode"]
            )
        )
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    return out
