"""Generated from Smithy shape ``com.amazonaws.cloudtrail#Destination``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudtrail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.destination_type
    import aws_sdk_cloudtrail.types.location


class Destination(TypedDict):
    type: "aws_sdk_cloudtrail.types.destination_type.DestinationType"
    """<p>The type of destination for events arriving from a channel. For channels used for a CloudTrail Lake integration, the value is <code>EVENT_DATA_STORE</code>. For service-linked channels, the value is <code>AWS_SERVICE</code>. </p>"""
    location: "aws_sdk_cloudtrail.types.location.Location"
    """<p> For channels used for a CloudTrail Lake integration, the location is the ARN of an event data store that receives events from a channel. For service-linked channels, the location is the name of the Amazon Web Services service.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Destination) -> dict:
    out: dict = {}
    import aws_sdk_cloudtrail.types.destination_type

    out["Type"] = aws_sdk_cloudtrail.types.destination_type.serialize_aws_json_1_1(
        value["type"]
    )
    out["Location"] = value["location"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Destination:
    out: Destination = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_cloudtrail.types.destination_type

        out["type"] = (
            aws_sdk_cloudtrail.types.destination_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("Destination.type required")
    if "Location" in data:
        out["location"] = data["Location"]
    else:
        raise DeserializationError("Destination.location required")
    return out
