"""Generated from Smithy shape ``com.amazonaws.location#UpdateTrackerResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.arn
    import aws_sdk_location.types.resource_name
    import aws_sdk_location.types.timestamp


class UpdateTrackerResponse(TypedDict):
    tracker_name: "aws_sdk_location.types.resource_name.ResourceName"
    """<p>The name of the updated tracker resource.</p>"""
    tracker_arn: "aws_sdk_location.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the updated tracker resource. Used to specify a resource across AWS.</p> <ul> <li> <p>Format example: <code>arn:aws:geo:region:account-id:tracker/ExampleTracker</code> </p> </li> </ul>"""
    update_time: "aws_sdk_location.types.timestamp.Timestamp"
    """<p>The timestamp for when the tracker resource was last updated in <a href=\"https://www.iso.org/iso-8601-date-and-time-format.html\"> ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTrackerResponse) -> dict:
    out: dict = {}
    out["TrackerName"] = value["tracker_name"]
    out["TrackerArn"] = value["tracker_arn"]
    import aws_sdk_location.types.timestamp

    out["UpdateTime"] = aws_sdk_location.types.timestamp.serialize_json(
        value["update_time"]
    )
    return out


def deserialize_json(data: dict) -> UpdateTrackerResponse:
    out: UpdateTrackerResponse = {}  # type: ignore[typeddict-item]
    if "TrackerName" in data:
        out["tracker_name"] = data["TrackerName"]
    else:
        raise DeserializationError("UpdateTrackerResponse.tracker_name required")
    if "TrackerArn" in data:
        out["tracker_arn"] = data["TrackerArn"]
    else:
        raise DeserializationError("UpdateTrackerResponse.tracker_arn required")
    if "UpdateTime" in data:
        import aws_sdk_location.types.timestamp

        out["update_time"] = aws_sdk_location.types.timestamp.deserialize_json(
            data["UpdateTime"]
        )
    else:
        raise DeserializationError("UpdateTrackerResponse.update_time required")
    return out
