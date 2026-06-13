"""Generated from Smithy shape ``com.amazonaws.location#ListGeofenceResponseEntry``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.geofence_geometry
    import aws_sdk_location.types.id
    import aws_sdk_location.types.property_map
    import aws_sdk_location.types.timestamp


class ListGeofenceResponseEntry(TypedDict):
    geofence_id: "aws_sdk_location.types.id.Id"
    """<p>The geofence identifier.</p>"""
    geometry: "aws_sdk_location.types.geofence_geometry.GeofenceGeometry"
    """<p>Contains the geofence geometry details describing the position of the geofence. Can be a circle, a polygon, or a multipolygon.</p>"""
    status: "str"
    """<p>Identifies the state of the geofence. A geofence will hold one of the following states:</p> <ul> <li> <p> <code>ACTIVE</code> — The geofence has been indexed by the system. </p> </li> <li> <p> <code>PENDING</code> — The geofence is being processed by the system.</p> </li> <li> <p> <code>FAILED</code> — The geofence failed to be indexed by the system.</p> </li> <li> <p> <code>DELETED</code> — The geofence has been deleted from the system index.</p> </li> <li> <p> <code>DELETING</code> — The geofence is being deleted from the system index.</p> </li> </ul>"""
    create_time: "aws_sdk_location.types.timestamp.Timestamp"
    """<p>The timestamp for when the geofence was stored in a geofence collection in <a href=\"https://www.iso.org/iso-8601-date-and-time-format.html\">ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code> </p>"""
    update_time: "aws_sdk_location.types.timestamp.Timestamp"
    """<p>The timestamp for when the geofence was last updated in <a href=\"https://www.iso.org/iso-8601-date-and-time-format.html\">ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code> </p>"""
    geofence_properties: NotRequired["aws_sdk_location.types.property_map.PropertyMap"]
    """<p>User defined properties of the geofence. A property is a key-value pair stored with the geofence and added to any geofence event triggered with that geofence.</p> <p>Format: <code>\"key\" : \"value\"</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGeofenceResponseEntry) -> dict:
    out: dict = {}
    out["GeofenceId"] = value["geofence_id"]
    import aws_sdk_location.types.geofence_geometry

    out["Geometry"] = aws_sdk_location.types.geofence_geometry.serialize_json(
        value["geometry"]
    )
    out["Status"] = value["status"]
    import aws_sdk_location.types.timestamp

    out["CreateTime"] = aws_sdk_location.types.timestamp.serialize_json(
        value["create_time"]
    )
    import aws_sdk_location.types.timestamp

    out["UpdateTime"] = aws_sdk_location.types.timestamp.serialize_json(
        value["update_time"]
    )
    if "geofence_properties" in value:
        import aws_sdk_location.types.property_map

        out["GeofenceProperties"] = aws_sdk_location.types.property_map.serialize_json(
            value["geofence_properties"]
        )
    return out


def deserialize_json(data: dict) -> ListGeofenceResponseEntry:
    out: ListGeofenceResponseEntry = {}  # type: ignore[typeddict-item]
    if "GeofenceId" in data:
        out["geofence_id"] = data["GeofenceId"]
    else:
        raise DeserializationError("ListGeofenceResponseEntry.geofence_id required")
    if "Geometry" in data:
        import aws_sdk_location.types.geofence_geometry

        out["geometry"] = aws_sdk_location.types.geofence_geometry.deserialize_json(
            data["Geometry"]
        )
    else:
        raise DeserializationError("ListGeofenceResponseEntry.geometry required")
    if "Status" in data:
        out["status"] = data["Status"]
    else:
        raise DeserializationError("ListGeofenceResponseEntry.status required")
    if "CreateTime" in data:
        import aws_sdk_location.types.timestamp

        out["create_time"] = aws_sdk_location.types.timestamp.deserialize_json(
            data["CreateTime"]
        )
    else:
        raise DeserializationError("ListGeofenceResponseEntry.create_time required")
    if "UpdateTime" in data:
        import aws_sdk_location.types.timestamp

        out["update_time"] = aws_sdk_location.types.timestamp.deserialize_json(
            data["UpdateTime"]
        )
    else:
        raise DeserializationError("ListGeofenceResponseEntry.update_time required")
    if "GeofenceProperties" in data:
        import aws_sdk_location.types.property_map

        out["geofence_properties"] = (
            aws_sdk_location.types.property_map.deserialize_json(
                data["GeofenceProperties"]
            )
        )
    return out
