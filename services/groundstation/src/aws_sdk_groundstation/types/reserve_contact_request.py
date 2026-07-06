"""Generated from Smithy shape ``com.amazonaws.groundstation#ReserveContactRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_groundstation.types.ground_station_name
    import aws_sdk_groundstation.types.mission_profile_arn
    import aws_sdk_groundstation.types.satellite_arn
    import aws_sdk_groundstation.types.tags_map
    import aws_sdk_groundstation.types.tracking_overrides


class ReserveContactRequest(TypedDict, closed=True):
    mission_profile_arn: (
        "aws_sdk_groundstation.types.mission_profile_arn.MissionProfileArn"
    )
    """<p>ARN of a mission profile.</p>"""
    satellite_arn: NotRequired["aws_sdk_groundstation.types.satellite_arn.satelliteArn"]
    """<p>ARN of a satellite</p>"""
    start_time: "datetime.datetime"
    """<p>Start time of a contact in UTC.</p>"""
    end_time: "datetime.datetime"
    """<p>End time of a contact in UTC.</p>"""
    ground_station: "aws_sdk_groundstation.types.ground_station_name.GroundStationName"
    """<p>Name of a ground station.</p>"""
    tags: NotRequired["aws_sdk_groundstation.types.tags_map.TagsMap"]
    """<p>Tags assigned to a contact.</p>"""
    tracking_overrides: NotRequired[
        "aws_sdk_groundstation.types.tracking_overrides.TrackingOverrides"
    ]
    """<p>Tracking configuration overrides for the contact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReserveContactRequest) -> dict:
    out: dict = {}
    out["missionProfileArn"] = value["mission_profile_arn"]
    if "satellite_arn" in value:
        out["satelliteArn"] = value["satellite_arn"]
    import aws_sdk_groundstation.types._prelude.timestamp

    out["startTime"] = aws_sdk_groundstation.types._prelude.timestamp.serialize_json(
        value["start_time"]
    )
    import aws_sdk_groundstation.types._prelude.timestamp

    out["endTime"] = aws_sdk_groundstation.types._prelude.timestamp.serialize_json(
        value["end_time"]
    )
    out["groundStation"] = value["ground_station"]
    if "tags" in value:
        import aws_sdk_groundstation.types.tags_map

        out["tags"] = aws_sdk_groundstation.types.tags_map.serialize_json(value["tags"])
    if "tracking_overrides" in value:
        import aws_sdk_groundstation.types.tracking_overrides

        out["trackingOverrides"] = (
            aws_sdk_groundstation.types.tracking_overrides.serialize_json(
                value["tracking_overrides"]
            )
        )
    return out


def deserialize_json(data: dict) -> ReserveContactRequest:
    out: ReserveContactRequest = {}  # type: ignore[typeddict-item]
    if "missionProfileArn" in data:
        out["mission_profile_arn"] = data["missionProfileArn"]
    else:
        raise DeserializationError("ReserveContactRequest.mission_profile_arn required")
    if "satelliteArn" in data:
        out["satellite_arn"] = data["satelliteArn"]
    if "startTime" in data:
        import aws_sdk_groundstation.types._prelude.timestamp

        out["start_time"] = (
            aws_sdk_groundstation.types._prelude.timestamp.deserialize_json(
                data["startTime"]
            )
        )
    else:
        raise DeserializationError("ReserveContactRequest.start_time required")
    if "endTime" in data:
        import aws_sdk_groundstation.types._prelude.timestamp

        out["end_time"] = (
            aws_sdk_groundstation.types._prelude.timestamp.deserialize_json(
                data["endTime"]
            )
        )
    else:
        raise DeserializationError("ReserveContactRequest.end_time required")
    if "groundStation" in data:
        out["ground_station"] = data["groundStation"]
    else:
        raise DeserializationError("ReserveContactRequest.ground_station required")
    if "tags" in data:
        import aws_sdk_groundstation.types.tags_map

        out["tags"] = aws_sdk_groundstation.types.tags_map.deserialize_json(
            data["tags"]
        )
    if "trackingOverrides" in data:
        import aws_sdk_groundstation.types.tracking_overrides

        out["tracking_overrides"] = (
            aws_sdk_groundstation.types.tracking_overrides.deserialize_json(
                data["trackingOverrides"]
            )
        )
    return out
