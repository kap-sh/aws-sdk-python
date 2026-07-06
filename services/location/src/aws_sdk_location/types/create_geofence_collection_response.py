"""Generated from Smithy shape ``com.amazonaws.location#CreateGeofenceCollectionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.arn
    import aws_sdk_location.types.resource_name
    import aws_sdk_location.types.timestamp


class CreateGeofenceCollectionResponse(TypedDict, closed=True):
    collection_name: "aws_sdk_location.types.resource_name.ResourceName"
    """<p>The name for the geofence collection.</p>"""
    collection_arn: "aws_sdk_location.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) for the geofence collection resource. Used when you need to specify a resource across all Amazon Web Services. </p> <ul> <li> <p>Format example: <code>arn:aws:geo:region:account-id:geofence-collection/ExampleGeofenceCollection</code> </p> </li> </ul>"""
    create_time: "aws_sdk_location.types.timestamp.Timestamp"
    r"""<p>The timestamp for when the geofence collection was created in <a href=\"https://www.iso.org/iso-8601-date-and-time-format.html\">ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateGeofenceCollectionResponse) -> dict:
    out: dict = {}
    out["CollectionName"] = value["collection_name"]
    out["CollectionArn"] = value["collection_arn"]
    import aws_sdk_location.types.timestamp

    out["CreateTime"] = aws_sdk_location.types.timestamp.serialize_json(
        value["create_time"]
    )
    return out


def deserialize_json(data: dict) -> CreateGeofenceCollectionResponse:
    out: CreateGeofenceCollectionResponse = {}  # type: ignore[typeddict-item]
    if "CollectionName" in data:
        out["collection_name"] = data["CollectionName"]
    else:
        raise DeserializationError(
            "CreateGeofenceCollectionResponse.collection_name required"
        )
    if "CollectionArn" in data:
        out["collection_arn"] = data["CollectionArn"]
    else:
        raise DeserializationError(
            "CreateGeofenceCollectionResponse.collection_arn required"
        )
    if "CreateTime" in data:
        import aws_sdk_location.types.timestamp

        out["create_time"] = aws_sdk_location.types.timestamp.deserialize_json(
            data["CreateTime"]
        )
    else:
        raise DeserializationError(
            "CreateGeofenceCollectionResponse.create_time required"
        )
    return out
