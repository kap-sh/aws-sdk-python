"""Generated from Smithy shape ``com.amazonaws.location#UpdateGeofenceCollectionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.arn
    import aws_sdk_location.types.resource_name
    import aws_sdk_location.types.timestamp


class UpdateGeofenceCollectionResponse(TypedDict):
    collection_name: "aws_sdk_location.types.resource_name.ResourceName"
    """<p>The name of the updated geofence collection.</p>"""
    collection_arn: "aws_sdk_location.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the updated geofence collection. Used to specify a resource across Amazon Web Services.</p> <ul> <li> <p>Format example: <code>arn:aws:geo:region:account-id:geofence-collection/ExampleGeofenceCollection</code> </p> </li> </ul>"""
    update_time: "aws_sdk_location.types.timestamp.Timestamp"
    r"""<p>The time when the geofence collection was last updated in <a href=\"https://www.iso.org/iso-8601-date-and-time-format.html\">ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGeofenceCollectionResponse) -> dict:
    out: dict = {}
    out["CollectionName"] = value["collection_name"]
    out["CollectionArn"] = value["collection_arn"]
    import aws_sdk_location.types.timestamp

    out["UpdateTime"] = aws_sdk_location.types.timestamp.serialize_json(
        value["update_time"]
    )
    return out


def deserialize_json(data: dict) -> UpdateGeofenceCollectionResponse:
    out: UpdateGeofenceCollectionResponse = {}  # type: ignore[typeddict-item]
    if "CollectionName" in data:
        out["collection_name"] = data["CollectionName"]
    else:
        raise DeserializationError(
            "UpdateGeofenceCollectionResponse.collection_name required"
        )
    if "CollectionArn" in data:
        out["collection_arn"] = data["CollectionArn"]
    else:
        raise DeserializationError(
            "UpdateGeofenceCollectionResponse.collection_arn required"
        )
    if "UpdateTime" in data:
        import aws_sdk_location.types.timestamp

        out["update_time"] = aws_sdk_location.types.timestamp.deserialize_json(
            data["UpdateTime"]
        )
    else:
        raise DeserializationError(
            "UpdateGeofenceCollectionResponse.update_time required"
        )
    return out
