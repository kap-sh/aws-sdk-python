"""Generated from Smithy shape ``com.amazonaws.location#BatchPutGeofenceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.batch_put_geofence_error_list
    import aws_sdk_location.types.batch_put_geofence_success_list


class BatchPutGeofenceResponse(TypedDict, closed=True):
    successes: "aws_sdk_location.types.batch_put_geofence_success_list.BatchPutGeofenceSuccessList"
    """<p>Contains each geofence that was successfully stored in a geofence collection.</p>"""
    errors: (
        "aws_sdk_location.types.batch_put_geofence_error_list.BatchPutGeofenceErrorList"
    )
    """<p>Contains additional error details for each geofence that failed to be stored in a geofence collection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutGeofenceResponse) -> dict:
    out: dict = {}
    import aws_sdk_location.types.batch_put_geofence_success_list

    out["Successes"] = (
        aws_sdk_location.types.batch_put_geofence_success_list.serialize_json(
            value["successes"]
        )
    )
    import aws_sdk_location.types.batch_put_geofence_error_list

    out["Errors"] = aws_sdk_location.types.batch_put_geofence_error_list.serialize_json(
        value["errors"]
    )
    return out


def deserialize_json(data: dict) -> BatchPutGeofenceResponse:
    out: BatchPutGeofenceResponse = {}  # type: ignore[typeddict-item]
    if "Successes" in data:
        import aws_sdk_location.types.batch_put_geofence_success_list

        out["successes"] = (
            aws_sdk_location.types.batch_put_geofence_success_list.deserialize_json(
                data["Successes"]
            )
        )
    else:
        raise DeserializationError("BatchPutGeofenceResponse.successes required")
    if "Errors" in data:
        import aws_sdk_location.types.batch_put_geofence_error_list

        out["errors"] = (
            aws_sdk_location.types.batch_put_geofence_error_list.deserialize_json(
                data["Errors"]
            )
        )
    else:
        raise DeserializationError("BatchPutGeofenceResponse.errors required")
    return out
