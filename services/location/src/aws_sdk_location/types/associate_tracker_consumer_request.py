"""Generated from Smithy shape ``com.amazonaws.location#AssociateTrackerConsumerRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.arn
    import aws_sdk_location.types.resource_name


class AssociateTrackerConsumerRequest(TypedDict):
    tracker_name: "aws_sdk_location.types.resource_name.ResourceName"
    """<p>The name of the tracker resource to be associated with a geofence collection.</p>"""
    consumer_arn: "aws_sdk_location.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) for the geofence collection to be associated to tracker resource. Used when you need to specify a resource across all Amazon Web Services.</p> <ul> <li> <p>Format example: <code>arn:aws:geo:region:account-id:geofence-collection/ExampleGeofenceCollectionConsumer</code> </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateTrackerConsumerRequest) -> dict:
    out: dict = {}
    out["ConsumerArn"] = value["consumer_arn"]
    return out


def deserialize_json(data: dict) -> AssociateTrackerConsumerRequest:
    out: AssociateTrackerConsumerRequest = {}  # type: ignore[typeddict-item]
    if "ConsumerArn" in data:
        out["consumer_arn"] = data["ConsumerArn"]
    else:
        raise DeserializationError(
            "AssociateTrackerConsumerRequest.consumer_arn required"
        )
    return out
