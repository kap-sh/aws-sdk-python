"""Generated from Smithy shape ``com.amazonaws.location#BatchEvaluateGeofencesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.batch_evaluate_geofences_error_list


class BatchEvaluateGeofencesResponse(TypedDict, closed=True):
    errors: "capo_location.types.batch_evaluate_geofences_error_list.BatchEvaluateGeofencesErrorList"
    """<p>Contains error details for each device that failed to evaluate its position against the given geofence collection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchEvaluateGeofencesResponse) -> dict:
    out: dict = {}
    import capo_location.types.batch_evaluate_geofences_error_list

    out["Errors"] = (
        capo_location.types.batch_evaluate_geofences_error_list.serialize_json(
            value["errors"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchEvaluateGeofencesResponse:
    out: BatchEvaluateGeofencesResponse = {}  # type: ignore[typeddict-item]
    if "Errors" in data:
        import capo_location.types.batch_evaluate_geofences_error_list

        out["errors"] = (
            capo_location.types.batch_evaluate_geofences_error_list.deserialize_json(
                data["Errors"]
            )
        )
    else:
        raise DeserializationError("BatchEvaluateGeofencesResponse.errors required")
    return out
