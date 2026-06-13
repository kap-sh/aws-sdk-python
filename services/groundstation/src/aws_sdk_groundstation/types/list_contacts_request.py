"""Generated from Smithy shape ``com.amazonaws.groundstation#ListContactsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_groundstation.types.ephemeris_filter
    import aws_sdk_groundstation.types.ground_station_name
    import aws_sdk_groundstation.types.mission_profile_arn
    import aws_sdk_groundstation.types.pagination_max_results
    import aws_sdk_groundstation.types.pagination_token
    import aws_sdk_groundstation.types.satellite_arn
    import aws_sdk_groundstation.types.status_list


class ListContactsRequest(TypedDict):
    max_results: NotRequired[
        "aws_sdk_groundstation.types.pagination_max_results.PaginationMaxResults"
    ]
    """<p>Maximum number of contacts returned.</p>"""
    next_token: NotRequired[
        "aws_sdk_groundstation.types.pagination_token.PaginationToken"
    ]
    """<p>Next token returned in the request of a previous <code>ListContacts</code> call. Used to get the next page of results.</p>"""
    status_list: "aws_sdk_groundstation.types.status_list.StatusList"
    """<p>Status of a contact reservation.</p>"""
    start_time: "datetime.datetime"
    """<p>Start time of a contact in UTC.</p>"""
    end_time: "datetime.datetime"
    """<p>End time of a contact in UTC.</p>"""
    ground_station: NotRequired[
        "aws_sdk_groundstation.types.ground_station_name.GroundStationName"
    ]
    """<p>Name of a ground station.</p>"""
    satellite_arn: NotRequired["aws_sdk_groundstation.types.satellite_arn.satelliteArn"]
    """<p>ARN of a satellite.</p>"""
    mission_profile_arn: NotRequired[
        "aws_sdk_groundstation.types.mission_profile_arn.MissionProfileArn"
    ]
    """<p>ARN of a mission profile.</p>"""
    ephemeris: NotRequired[
        "aws_sdk_groundstation.types.ephemeris_filter.EphemerisFilter"
    ]
    """<p>Filter for selecting contacts that use a specific ephemeris\".</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListContactsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_groundstation.types.status_list

    out["statusList"] = aws_sdk_groundstation.types.status_list.serialize_json(
        value["status_list"]
    )
    import aws_sdk_groundstation.types._prelude.timestamp

    out["startTime"] = aws_sdk_groundstation.types._prelude.timestamp.serialize_json(
        value["start_time"]
    )
    import aws_sdk_groundstation.types._prelude.timestamp

    out["endTime"] = aws_sdk_groundstation.types._prelude.timestamp.serialize_json(
        value["end_time"]
    )
    if "ground_station" in value:
        out["groundStation"] = value["ground_station"]
    if "satellite_arn" in value:
        out["satelliteArn"] = value["satellite_arn"]
    if "mission_profile_arn" in value:
        out["missionProfileArn"] = value["mission_profile_arn"]
    if "ephemeris" in value:
        import aws_sdk_groundstation.types.ephemeris_filter

        out["ephemeris"] = aws_sdk_groundstation.types.ephemeris_filter.serialize_json(
            value["ephemeris"]
        )
    return out


def deserialize_json(data: dict) -> ListContactsRequest:
    out: ListContactsRequest = {}  # type: ignore[typeddict-item]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "statusList" in data:
        import aws_sdk_groundstation.types.status_list

        out["status_list"] = aws_sdk_groundstation.types.status_list.deserialize_json(
            data["statusList"]
        )
    else:
        raise DeserializationError("ListContactsRequest.status_list required")
    if "startTime" in data:
        import aws_sdk_groundstation.types._prelude.timestamp

        out["start_time"] = (
            aws_sdk_groundstation.types._prelude.timestamp.deserialize_json(
                data["startTime"]
            )
        )
    else:
        raise DeserializationError("ListContactsRequest.start_time required")
    if "endTime" in data:
        import aws_sdk_groundstation.types._prelude.timestamp

        out["end_time"] = (
            aws_sdk_groundstation.types._prelude.timestamp.deserialize_json(
                data["endTime"]
            )
        )
    else:
        raise DeserializationError("ListContactsRequest.end_time required")
    if "groundStation" in data:
        out["ground_station"] = data["groundStation"]
    if "satelliteArn" in data:
        out["satellite_arn"] = data["satelliteArn"]
    if "missionProfileArn" in data:
        out["mission_profile_arn"] = data["missionProfileArn"]
    if "ephemeris" in data:
        import aws_sdk_groundstation.types.ephemeris_filter

        out["ephemeris"] = (
            aws_sdk_groundstation.types.ephemeris_filter.deserialize_json(
                data["ephemeris"]
            )
        )
    return out
