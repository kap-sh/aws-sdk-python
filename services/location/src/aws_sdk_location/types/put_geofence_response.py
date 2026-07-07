"""Generated from Smithy shape ``com.amazonaws.location#PutGeofenceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.id
    import aws_sdk_location.types.timestamp


class PutGeofenceResponse(TypedDict, closed=True):
    geofence_id: "aws_sdk_location.types.id.Id"
    """<p>The geofence identifier entered in the request.</p>"""
    create_time: "aws_sdk_location.types.timestamp.Timestamp"
    r"""<p>The timestamp for when the geofence was created in <a href=\"https://www.iso.org/iso-8601-date-and-time-format.html\">ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code> </p>"""
    update_time: "aws_sdk_location.types.timestamp.Timestamp"
    r"""<p>The timestamp for when the geofence was last updated in <a href=\"https://www.iso.org/iso-8601-date-and-time-format.html\">ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutGeofenceResponse) -> dict:
    out: dict = {}
    out["GeofenceId"] = value["geofence_id"]
    import aws_sdk_location.types.timestamp

    out["CreateTime"] = aws_sdk_location.types.timestamp.serialize_json(
        value["create_time"]
    )
    import aws_sdk_location.types.timestamp

    out["UpdateTime"] = aws_sdk_location.types.timestamp.serialize_json(
        value["update_time"]
    )
    return out


def deserialize_json(data: dict) -> PutGeofenceResponse:
    out: PutGeofenceResponse = {}  # type: ignore[typeddict-item]
    if "GeofenceId" in data:
        out["geofence_id"] = data["GeofenceId"]
    else:
        raise DeserializationError("PutGeofenceResponse.geofence_id required")
    if "CreateTime" in data:
        import aws_sdk_location.types.timestamp

        out["create_time"] = aws_sdk_location.types.timestamp.deserialize_json(
            data["CreateTime"]
        )
    else:
        raise DeserializationError("PutGeofenceResponse.create_time required")
    if "UpdateTime" in data:
        import aws_sdk_location.types.timestamp

        out["update_time"] = aws_sdk_location.types.timestamp.deserialize_json(
            data["UpdateTime"]
        )
    else:
        raise DeserializationError("PutGeofenceResponse.update_time required")
    return out
