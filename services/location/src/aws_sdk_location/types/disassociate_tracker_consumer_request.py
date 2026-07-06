"""Generated from Smithy shape ``com.amazonaws.location#DisassociateTrackerConsumerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_location.types.arn
    import aws_sdk_location.types.resource_name


class DisassociateTrackerConsumerRequest(TypedDict, closed=True):
    tracker_name: "aws_sdk_location.types.resource_name.ResourceName"
    """<p>The name of the tracker resource to be dissociated from the consumer.</p>"""
    consumer_arn: "aws_sdk_location.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) for the geofence collection to be disassociated from the tracker resource. Used when you need to specify a resource across all Amazon Web Services. </p> <ul> <li> <p>Format example: <code>arn:aws:geo:region:account-id:geofence-collection/ExampleGeofenceCollectionConsumer</code> </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateTrackerConsumerRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateTrackerConsumerRequest:
    out: DisassociateTrackerConsumerRequest = {}  # type: ignore[typeddict-item]
    return out
