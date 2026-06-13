"""Generated from Smithy shape ``com.amazonaws.groundstation#ListEphemeridesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_groundstation.types.ephemeris_status_list
    import aws_sdk_groundstation.types.ephemeris_type
    import aws_sdk_groundstation.types.pagination_max_results
    import aws_sdk_groundstation.types.pagination_token
    import aws_sdk_groundstation.types.uuid


class ListEphemeridesRequest(TypedDict):
    satellite_id: NotRequired["aws_sdk_groundstation.types.uuid.Uuid"]
    """<p>The AWS Ground Station satellite ID to list ephemeris for.</p>"""
    ephemeris_type: NotRequired[
        "aws_sdk_groundstation.types.ephemeris_type.EphemerisType"
    ]
    """<p>Filter ephemerides by type. If not specified, all ephemeris types will be returned.</p>"""
    start_time: "datetime.datetime"
    """<p>The start time for the list operation in UTC. Returns ephemerides with expiration times within your specified time range.</p>"""
    end_time: "datetime.datetime"
    """<p>The end time for the list operation in UTC. Returns ephemerides with expiration times within your specified time range.</p>"""
    status_list: NotRequired[
        "aws_sdk_groundstation.types.ephemeris_status_list.EphemerisStatusList"
    ]
    """<p>The list of ephemeris status to return.</p>"""
    max_results: NotRequired[
        "aws_sdk_groundstation.types.pagination_max_results.PaginationMaxResults"
    ]
    """<p>Maximum number of ephemerides to return.</p>"""
    next_token: NotRequired[
        "aws_sdk_groundstation.types.pagination_token.PaginationToken"
    ]
    """<p>Pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEphemeridesRequest) -> dict:
    out: dict = {}
    if "satellite_id" in value:
        out["satelliteId"] = value["satellite_id"]
    if "ephemeris_type" in value:
        import aws_sdk_groundstation.types.ephemeris_type

        out["ephemerisType"] = (
            aws_sdk_groundstation.types.ephemeris_type.serialize_json(
                value["ephemeris_type"]
            )
        )
    import aws_sdk_groundstation.types._prelude.timestamp

    out["startTime"] = aws_sdk_groundstation.types._prelude.timestamp.serialize_json(
        value["start_time"]
    )
    import aws_sdk_groundstation.types._prelude.timestamp

    out["endTime"] = aws_sdk_groundstation.types._prelude.timestamp.serialize_json(
        value["end_time"]
    )
    if "status_list" in value:
        import aws_sdk_groundstation.types.ephemeris_status_list

        out["statusList"] = (
            aws_sdk_groundstation.types.ephemeris_status_list.serialize_json(
                value["status_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListEphemeridesRequest:
    out: ListEphemeridesRequest = {}  # type: ignore[typeddict-item]
    if "satelliteId" in data:
        out["satellite_id"] = data["satelliteId"]
    if "ephemerisType" in data:
        import aws_sdk_groundstation.types.ephemeris_type

        out["ephemeris_type"] = (
            aws_sdk_groundstation.types.ephemeris_type.deserialize_json(
                data["ephemerisType"]
            )
        )
    if "startTime" in data:
        import aws_sdk_groundstation.types._prelude.timestamp

        out["start_time"] = (
            aws_sdk_groundstation.types._prelude.timestamp.deserialize_json(
                data["startTime"]
            )
        )
    else:
        raise DeserializationError("ListEphemeridesRequest.start_time required")
    if "endTime" in data:
        import aws_sdk_groundstation.types._prelude.timestamp

        out["end_time"] = (
            aws_sdk_groundstation.types._prelude.timestamp.deserialize_json(
                data["endTime"]
            )
        )
    else:
        raise DeserializationError("ListEphemeridesRequest.end_time required")
    if "statusList" in data:
        import aws_sdk_groundstation.types.ephemeris_status_list

        out["status_list"] = (
            aws_sdk_groundstation.types.ephemeris_status_list.deserialize_json(
                data["statusList"]
            )
        )
    return out
