"""Generated from Smithy shape ``com.amazonaws.applicationsignals#BatchUpdateExclusionWindowsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_application_signals.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_signals.types.batch_update_exclusion_windows_errors
    import aws_sdk_application_signals.types.service_level_objective_ids


class BatchUpdateExclusionWindowsOutput(TypedDict):
    slo_ids: "aws_sdk_application_signals.types.service_level_objective_ids.ServiceLevelObjectiveIds"
    """<p>The list of SLO IDs that were successfully processed.</p>"""
    errors: "aws_sdk_application_signals.types.batch_update_exclusion_windows_errors.BatchUpdateExclusionWindowsErrors"
    """<p>A list of errors that occurred while processing the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateExclusionWindowsOutput) -> dict:
    out: dict = {}
    import aws_sdk_application_signals.types.service_level_objective_ids

    out["SloIds"] = (
        aws_sdk_application_signals.types.service_level_objective_ids.serialize_json(
            value["slo_ids"]
        )
    )
    import aws_sdk_application_signals.types.batch_update_exclusion_windows_errors

    out["Errors"] = (
        aws_sdk_application_signals.types.batch_update_exclusion_windows_errors.serialize_json(
            value["errors"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchUpdateExclusionWindowsOutput:
    out: BatchUpdateExclusionWindowsOutput = {}  # type: ignore[typeddict-item]
    if "SloIds" in data:
        import aws_sdk_application_signals.types.service_level_objective_ids

        out["slo_ids"] = (
            aws_sdk_application_signals.types.service_level_objective_ids.deserialize_json(
                data["SloIds"]
            )
        )
    else:
        raise DeserializationError("BatchUpdateExclusionWindowsOutput.slo_ids required")
    if "Errors" in data:
        import aws_sdk_application_signals.types.batch_update_exclusion_windows_errors

        out["errors"] = (
            aws_sdk_application_signals.types.batch_update_exclusion_windows_errors.deserialize_json(
                data["Errors"]
            )
        )
    else:
        raise DeserializationError("BatchUpdateExclusionWindowsOutput.errors required")
    return out
