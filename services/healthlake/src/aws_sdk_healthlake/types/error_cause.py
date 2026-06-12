"""Generated from Smithy shape ``com.amazonaws.healthlake#ErrorCause``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_healthlake.types.error_category
    import aws_sdk_healthlake.types.error_message


class ErrorCause(TypedDict):
    error_message: NotRequired["aws_sdk_healthlake.types.error_message.ErrorMessage"]
    """<p>The error message text for <code>ErrorCause</code>.</p>"""
    error_category: NotRequired["aws_sdk_healthlake.types.error_category.ErrorCategory"]
    """<p>The error category for <code>ErrorCause</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ErrorCause) -> dict:
    out: dict = {}
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "error_category" in value:
        import aws_sdk_healthlake.types.error_category

        out["ErrorCategory"] = (
            aws_sdk_healthlake.types.error_category.serialize_aws_json_1_0(
                value["error_category"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ErrorCause:
    out: ErrorCause = {}  # type: ignore[typeddict-item]
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    if "ErrorCategory" in data:
        import aws_sdk_healthlake.types.error_category

        out["error_category"] = (
            aws_sdk_healthlake.types.error_category.deserialize_aws_json_1_0(
                data["ErrorCategory"]
            )
        )
    return out
