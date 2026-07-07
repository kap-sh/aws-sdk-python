"""Generated from Smithy shape ``com.amazonaws.applicationsignals#BatchUpdateExclusionWindowsError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_application_signals.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_signals.types.exclusion_window_error_code
    import aws_sdk_application_signals.types.exclusion_window_error_message
    import aws_sdk_application_signals.types.service_level_objective_id


class BatchUpdateExclusionWindowsError(TypedDict, closed=True):
    slo_id: "aws_sdk_application_signals.types.service_level_objective_id.ServiceLevelObjectiveId"
    """<p>The SLO ID in the error.</p>"""
    error_code: "aws_sdk_application_signals.types.exclusion_window_error_code.ExclusionWindowErrorCode"
    """<p>The error code.</p>"""
    error_message: "aws_sdk_application_signals.types.exclusion_window_error_message.ExclusionWindowErrorMessage"
    """<p>The error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateExclusionWindowsError) -> dict:
    out: dict = {}
    out["SloId"] = value["slo_id"]
    out["ErrorCode"] = value["error_code"]
    out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> BatchUpdateExclusionWindowsError:
    out: BatchUpdateExclusionWindowsError = {}  # type: ignore[typeddict-item]
    if "SloId" in data:
        out["slo_id"] = data["SloId"]
    else:
        raise DeserializationError("BatchUpdateExclusionWindowsError.slo_id required")
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    else:
        raise DeserializationError(
            "BatchUpdateExclusionWindowsError.error_code required"
        )
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    else:
        raise DeserializationError(
            "BatchUpdateExclusionWindowsError.error_message required"
        )
    return out
