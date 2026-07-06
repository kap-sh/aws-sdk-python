"""Generated from Smithy shape ``com.amazonaws.servicequotas#ErrorReason``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_service_quotas.types.error_code
    import aws_sdk_service_quotas.types.error_message


class ErrorReason(TypedDict, closed=True):
    error_code: NotRequired["aws_sdk_service_quotas.types.error_code.ErrorCode"]
    """<p>Service Quotas returns the following error values:</p> <ul> <li> <p> <code>DEPENDENCY_ACCESS_DENIED_ERROR</code> - The caller does not have the required permissions to complete the action. To resolve the error, you must have permission to access the Amazon Web Services service or quota.</p> </li> <li> <p> <code>DEPENDENCY_THROTTLING_ERROR</code> - The Amazon Web Services service is throttling Service Quotas. </p> </li> <li> <p> <code>DEPENDENCY_SERVICE_ERROR</code> - The Amazon Web Services service is not available.</p> </li> <li> <p> <code>SERVICE_QUOTA_NOT_AVAILABLE_ERROR</code> - There was an error in Service Quotas.</p> </li> </ul>"""
    error_message: NotRequired[
        "aws_sdk_service_quotas.types.error_message.ErrorMessage"
    ]
    """<p>The error message.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ErrorReason) -> dict:
    out: dict = {}
    if "error_code" in value:
        import aws_sdk_service_quotas.types.error_code

        out["ErrorCode"] = (
            aws_sdk_service_quotas.types.error_code.serialize_aws_json_1_1(
                value["error_code"]
            )
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ErrorReason:
    out: ErrorReason = {}  # type: ignore[typeddict-item]
    if "ErrorCode" in data:
        import aws_sdk_service_quotas.types.error_code

        out["error_code"] = (
            aws_sdk_service_quotas.types.error_code.deserialize_aws_json_1_1(
                data["ErrorCode"]
            )
        )
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    return out
