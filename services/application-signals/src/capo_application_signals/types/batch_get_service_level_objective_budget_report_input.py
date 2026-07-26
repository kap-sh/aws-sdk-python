"""Generated from Smithy shape ``com.amazonaws.applicationsignals#BatchGetServiceLevelObjectiveBudgetReportInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_application_signals.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_application_signals.types.service_level_objective_ids


class BatchGetServiceLevelObjectiveBudgetReportInput(TypedDict, closed=True):
    timestamp: "datetime.datetime"
    """<p>The date and time that you want the report to be for. It is expressed as the number of milliseconds since Jan 1, 1970 00:00:00 UTC.</p>"""
    slo_ids: "capo_application_signals.types.service_level_objective_ids.ServiceLevelObjectiveIds"
    """<p>An array containing the IDs of the service level objectives that you want to include in the report.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetServiceLevelObjectiveBudgetReportInput) -> dict:
    out: dict = {}
    import capo_application_signals.types._prelude.timestamp

    out["Timestamp"] = capo_application_signals.types._prelude.timestamp.serialize_json(
        value["timestamp"]
    )
    import capo_application_signals.types.service_level_objective_ids

    out["SloIds"] = (
        capo_application_signals.types.service_level_objective_ids.serialize_json(
            value["slo_ids"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchGetServiceLevelObjectiveBudgetReportInput:
    out: BatchGetServiceLevelObjectiveBudgetReportInput = {}  # type: ignore[typeddict-item]
    if "Timestamp" in data:
        import capo_application_signals.types._prelude.timestamp

        out["timestamp"] = (
            capo_application_signals.types._prelude.timestamp.deserialize_json(
                data["Timestamp"]
            )
        )
    else:
        raise DeserializationError(
            "BatchGetServiceLevelObjectiveBudgetReportInput.timestamp required"
        )
    if "SloIds" in data:
        import capo_application_signals.types.service_level_objective_ids

        out["slo_ids"] = (
            capo_application_signals.types.service_level_objective_ids.deserialize_json(
                data["SloIds"]
            )
        )
    else:
        raise DeserializationError(
            "BatchGetServiceLevelObjectiveBudgetReportInput.slo_ids required"
        )
    return out
