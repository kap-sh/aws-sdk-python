"""Generated from Smithy shape ``com.amazonaws.sfn#InspectionErrorDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sfn.types.exception_handler_index
    import aws_sdk_sfn.types.retry_backoff_interval_seconds


class InspectionErrorDetails(TypedDict, closed=True):
    catch_index: NotRequired[
        "aws_sdk_sfn.types.exception_handler_index.ExceptionHandlerIndex"
    ]
    """<p>The array index of the Catch which handled the exception.</p>"""
    retry_index: NotRequired[
        "aws_sdk_sfn.types.exception_handler_index.ExceptionHandlerIndex"
    ]
    """<p>The array index of the Retry which handled the exception.</p>"""
    retry_backoff_interval_seconds: NotRequired[
        "aws_sdk_sfn.types.retry_backoff_interval_seconds.RetryBackoffIntervalSeconds"
    ]
    """<p>The duration in seconds of the backoff for a retry on a failed state invocation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InspectionErrorDetails) -> dict:
    out: dict = {}
    if "catch_index" in value:
        out["catchIndex"] = value["catch_index"]
    if "retry_index" in value:
        out["retryIndex"] = value["retry_index"]
    if "retry_backoff_interval_seconds" in value:
        out["retryBackoffIntervalSeconds"] = value["retry_backoff_interval_seconds"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InspectionErrorDetails:
    out: InspectionErrorDetails = {}  # type: ignore[typeddict-item]
    if "catchIndex" in data:
        out["catch_index"] = data["catchIndex"]
    if "retryIndex" in data:
        out["retry_index"] = data["retryIndex"]
    if "retryBackoffIntervalSeconds" in data:
        out["retry_backoff_interval_seconds"] = data["retryBackoffIntervalSeconds"]
    return out
