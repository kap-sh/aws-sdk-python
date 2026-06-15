"""Generated from Smithy shape ``com.amazonaws.groundstation#ContactData``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_groundstation.types.contact_status
    import aws_sdk_groundstation.types.contact_version
    import aws_sdk_groundstation.types.elevation
    import aws_sdk_groundstation.types.ephemeris_response_data
    import aws_sdk_groundstation.types.mission_profile_arn
    import aws_sdk_groundstation.types.satellite_arn
    import aws_sdk_groundstation.types.tags_map
    import aws_sdk_groundstation.types.uuid


class ContactData(TypedDict):
    contact_id: NotRequired["aws_sdk_groundstation.types.uuid.Uuid"]
    """<p>UUID of a contact.</p>"""
    mission_profile_arn: NotRequired[
        "aws_sdk_groundstation.types.mission_profile_arn.MissionProfileArn"
    ]
    """<p>ARN of a mission profile.</p>"""
    satellite_arn: NotRequired["aws_sdk_groundstation.types.satellite_arn.satelliteArn"]
    """<p>ARN of a satellite.</p>"""
    start_time: NotRequired["datetime.datetime"]
    """<p>Start time of a contact in UTC.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>End time of a contact in UTC.</p>"""
    pre_pass_start_time: NotRequired["datetime.datetime"]
    """<p>Start time in UTC of the pre-pass period, at which you receive a CloudWatch event indicating an upcoming pass.</p>"""
    post_pass_end_time: NotRequired["datetime.datetime"]
    """<p>End time in UTC of the post-pass period, at which you receive a CloudWatch event indicating the pass has finished.</p>"""
    ground_station: NotRequired["str"]
    """<p>Name of a ground station.</p>"""
    contact_status: NotRequired[
        "aws_sdk_groundstation.types.contact_status.ContactStatus"
    ]
    """<p>Status of a contact.</p>"""
    error_message: NotRequired["str"]
    """<p>Error message of a contact.</p>"""
    maximum_elevation: NotRequired["aws_sdk_groundstation.types.elevation.Elevation"]
    """<p>Maximum elevation angle of a contact.</p>"""
    region: NotRequired["str"]
    """<p>Region of a contact.</p>"""
    tags: NotRequired["aws_sdk_groundstation.types.tags_map.TagsMap"]
    """<p>Tags assigned to a contact.</p>"""
    visibility_start_time: NotRequired["datetime.datetime"]
    r"""<p> Projected time in UTC your satellite will rise above the <a href=\"https://docs.aws.amazon.com/ground-station/latest/ug/site-masks.html\">receive mask</a>. This time is based on the satellite's current active ephemeris for future contacts and the ephemeris that was active during contact execution for completed contacts. <i>This field is not present for contacts with a <code>SCHEDULING</code> or <code>SCHEDULED</code> status.</i> </p>"""
    visibility_end_time: NotRequired["datetime.datetime"]
    r"""<p> Projected time in UTC your satellite will set below the <a href=\"https://docs.aws.amazon.com/ground-station/latest/ug/site-masks.html\">receive mask</a>. This time is based on the satellite's current active ephemeris for future contacts and the ephemeris that was active during contact execution for completed contacts. <i>This field is not present for contacts with a <code>SCHEDULING</code> or <code>SCHEDULED</code> status.</i> </p>"""
    ephemeris: NotRequired[
        "aws_sdk_groundstation.types.ephemeris_response_data.EphemerisResponseData"
    ]
    """<p>The ephemeris that determines antenna pointing for the contact.</p>"""
    version: NotRequired["aws_sdk_groundstation.types.contact_version.ContactVersion"]
    """<p>Version information for a contact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactData) -> dict:
    out: dict = {}
    if "contact_id" in value:
        out["contactId"] = value["contact_id"]
    if "mission_profile_arn" in value:
        out["missionProfileArn"] = value["mission_profile_arn"]
    if "satellite_arn" in value:
        out["satelliteArn"] = value["satellite_arn"]
    if "start_time" in value:
        import aws_sdk_groundstation.types._prelude.timestamp

        out["startTime"] = (
            aws_sdk_groundstation.types._prelude.timestamp.serialize_json(
                value["start_time"]
            )
        )
    if "end_time" in value:
        import aws_sdk_groundstation.types._prelude.timestamp

        out["endTime"] = aws_sdk_groundstation.types._prelude.timestamp.serialize_json(
            value["end_time"]
        )
    if "pre_pass_start_time" in value:
        import aws_sdk_groundstation.types._prelude.timestamp

        out["prePassStartTime"] = (
            aws_sdk_groundstation.types._prelude.timestamp.serialize_json(
                value["pre_pass_start_time"]
            )
        )
    if "post_pass_end_time" in value:
        import aws_sdk_groundstation.types._prelude.timestamp

        out["postPassEndTime"] = (
            aws_sdk_groundstation.types._prelude.timestamp.serialize_json(
                value["post_pass_end_time"]
            )
        )
    if "ground_station" in value:
        out["groundStation"] = value["ground_station"]
    if "contact_status" in value:
        import aws_sdk_groundstation.types.contact_status

        out["contactStatus"] = (
            aws_sdk_groundstation.types.contact_status.serialize_json(
                value["contact_status"]
            )
        )
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    if "maximum_elevation" in value:
        import aws_sdk_groundstation.types.elevation

        out["maximumElevation"] = aws_sdk_groundstation.types.elevation.serialize_json(
            value["maximum_elevation"]
        )
    if "region" in value:
        out["region"] = value["region"]
    if "tags" in value:
        import aws_sdk_groundstation.types.tags_map

        out["tags"] = aws_sdk_groundstation.types.tags_map.serialize_json(value["tags"])
    if "visibility_start_time" in value:
        import aws_sdk_groundstation.types._prelude.timestamp

        out["visibilityStartTime"] = (
            aws_sdk_groundstation.types._prelude.timestamp.serialize_json(
                value["visibility_start_time"]
            )
        )
    if "visibility_end_time" in value:
        import aws_sdk_groundstation.types._prelude.timestamp

        out["visibilityEndTime"] = (
            aws_sdk_groundstation.types._prelude.timestamp.serialize_json(
                value["visibility_end_time"]
            )
        )
    if "ephemeris" in value:
        import aws_sdk_groundstation.types.ephemeris_response_data

        out["ephemeris"] = (
            aws_sdk_groundstation.types.ephemeris_response_data.serialize_json(
                value["ephemeris"]
            )
        )
    if "version" in value:
        import aws_sdk_groundstation.types.contact_version

        out["version"] = aws_sdk_groundstation.types.contact_version.serialize_json(
            value["version"]
        )
    return out


def deserialize_json(data: dict) -> ContactData:
    out: ContactData = {}  # type: ignore[typeddict-item]
    if "contactId" in data:
        out["contact_id"] = data["contactId"]
    if "missionProfileArn" in data:
        out["mission_profile_arn"] = data["missionProfileArn"]
    if "satelliteArn" in data:
        out["satellite_arn"] = data["satelliteArn"]
    if "startTime" in data:
        import aws_sdk_groundstation.types._prelude.timestamp

        out["start_time"] = (
            aws_sdk_groundstation.types._prelude.timestamp.deserialize_json(
                data["startTime"]
            )
        )
    if "endTime" in data:
        import aws_sdk_groundstation.types._prelude.timestamp

        out["end_time"] = (
            aws_sdk_groundstation.types._prelude.timestamp.deserialize_json(
                data["endTime"]
            )
        )
    if "prePassStartTime" in data:
        import aws_sdk_groundstation.types._prelude.timestamp

        out["pre_pass_start_time"] = (
            aws_sdk_groundstation.types._prelude.timestamp.deserialize_json(
                data["prePassStartTime"]
            )
        )
    if "postPassEndTime" in data:
        import aws_sdk_groundstation.types._prelude.timestamp

        out["post_pass_end_time"] = (
            aws_sdk_groundstation.types._prelude.timestamp.deserialize_json(
                data["postPassEndTime"]
            )
        )
    if "groundStation" in data:
        out["ground_station"] = data["groundStation"]
    if "contactStatus" in data:
        import aws_sdk_groundstation.types.contact_status

        out["contact_status"] = (
            aws_sdk_groundstation.types.contact_status.deserialize_json(
                data["contactStatus"]
            )
        )
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    if "maximumElevation" in data:
        import aws_sdk_groundstation.types.elevation

        out["maximum_elevation"] = (
            aws_sdk_groundstation.types.elevation.deserialize_json(
                data["maximumElevation"]
            )
        )
    if "region" in data:
        out["region"] = data["region"]
    if "tags" in data:
        import aws_sdk_groundstation.types.tags_map

        out["tags"] = aws_sdk_groundstation.types.tags_map.deserialize_json(
            data["tags"]
        )
    if "visibilityStartTime" in data:
        import aws_sdk_groundstation.types._prelude.timestamp

        out["visibility_start_time"] = (
            aws_sdk_groundstation.types._prelude.timestamp.deserialize_json(
                data["visibilityStartTime"]
            )
        )
    if "visibilityEndTime" in data:
        import aws_sdk_groundstation.types._prelude.timestamp

        out["visibility_end_time"] = (
            aws_sdk_groundstation.types._prelude.timestamp.deserialize_json(
                data["visibilityEndTime"]
            )
        )
    if "ephemeris" in data:
        import aws_sdk_groundstation.types.ephemeris_response_data

        out["ephemeris"] = (
            aws_sdk_groundstation.types.ephemeris_response_data.deserialize_json(
                data["ephemeris"]
            )
        )
    if "version" in data:
        import aws_sdk_groundstation.types.contact_version

        out["version"] = aws_sdk_groundstation.types.contact_version.deserialize_json(
            data["version"]
        )
    return out
