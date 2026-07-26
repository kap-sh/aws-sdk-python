"""Generated from Smithy shape ``com.amazonaws.groundstation#DescribeEphemerisResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_groundstation.types.ephemeris_error_reason_list
    import capo_groundstation.types.ephemeris_invalid_reason
    import capo_groundstation.types.ephemeris_priority
    import capo_groundstation.types.ephemeris_status
    import capo_groundstation.types.ephemeris_type_description
    import capo_groundstation.types.safe_name
    import capo_groundstation.types.tags_map
    import capo_groundstation.types.uuid


class DescribeEphemerisResponse(TypedDict, closed=True):
    ephemeris_id: NotRequired["capo_groundstation.types.uuid.Uuid"]
    """<p>The AWS Ground Station ephemeris ID.</p>"""
    satellite_id: NotRequired["capo_groundstation.types.uuid.Uuid"]
    """<p>The AWS Ground Station satellite ID associated with ephemeris.</p>"""
    status: NotRequired["capo_groundstation.types.ephemeris_status.EphemerisStatus"]
    """<p>The status of the ephemeris.</p>"""
    priority: NotRequired[
        "capo_groundstation.types.ephemeris_priority.EphemerisPriority"
    ]
    """<p>A priority score that determines which ephemeris to use when multiple ephemerides overlap.</p> <p>Higher numbers take precedence. The default is 1. Must be 1 or greater.</p>"""
    creation_time: NotRequired["datetime.datetime"]
    """<p>The time the ephemeris was uploaded in UTC.</p>"""
    enabled: NotRequired["bool"]
    """<p>Whether or not the ephemeris is enabled.</p>"""
    name: NotRequired["capo_groundstation.types.safe_name.SafeName"]
    """<p>A name that you can use to identify the ephemeris.</p>"""
    tags: NotRequired["capo_groundstation.types.tags_map.TagsMap"]
    """<p>Tags assigned to an ephemeris.</p>"""
    supplied_data: NotRequired[
        "capo_groundstation.types.ephemeris_type_description.EphemerisTypeDescription"
    ]
    """<p>Supplied ephemeris data.</p>"""
    invalid_reason: NotRequired[
        "capo_groundstation.types.ephemeris_invalid_reason.EphemerisInvalidReason"
    ]
    """<p>Reason that an ephemeris failed validation. Appears only when the status is <code>INVALID</code>.</p>"""
    error_reasons: NotRequired[
        "capo_groundstation.types.ephemeris_error_reason_list.EphemerisErrorReasonList"
    ]
    """<p>Detailed error information for ephemerides with <code>INVALID</code> status.</p> <p>Provides specific error codes and messages to help diagnose validation failures.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeEphemerisResponse) -> dict:
    out: dict = {}
    if "ephemeris_id" in value:
        out["ephemerisId"] = value["ephemeris_id"]
    if "satellite_id" in value:
        out["satelliteId"] = value["satellite_id"]
    if "status" in value:
        import capo_groundstation.types.ephemeris_status

        out["status"] = capo_groundstation.types.ephemeris_status.serialize_json(
            value["status"]
        )
    if "priority" in value:
        out["priority"] = value["priority"]
    if "creation_time" in value:
        import capo_groundstation.types._prelude.timestamp

        out["creationTime"] = (
            capo_groundstation.types._prelude.timestamp.serialize_json(
                value["creation_time"]
            )
        )
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    if "name" in value:
        out["name"] = value["name"]
    if "tags" in value:
        import capo_groundstation.types.tags_map

        out["tags"] = capo_groundstation.types.tags_map.serialize_json(value["tags"])
    if "supplied_data" in value:
        import capo_groundstation.types.ephemeris_type_description

        out["suppliedData"] = (
            capo_groundstation.types.ephemeris_type_description.serialize_json(
                value["supplied_data"]
            )
        )
    if "invalid_reason" in value:
        import capo_groundstation.types.ephemeris_invalid_reason

        out["invalidReason"] = (
            capo_groundstation.types.ephemeris_invalid_reason.serialize_json(
                value["invalid_reason"]
            )
        )
    if "error_reasons" in value:
        import capo_groundstation.types.ephemeris_error_reason_list

        out["errorReasons"] = (
            capo_groundstation.types.ephemeris_error_reason_list.serialize_json(
                value["error_reasons"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeEphemerisResponse:
    out: DescribeEphemerisResponse = {}  # type: ignore[typeddict-item]
    if "ephemerisId" in data:
        out["ephemeris_id"] = data["ephemerisId"]
    if "satelliteId" in data:
        out["satellite_id"] = data["satelliteId"]
    if "status" in data:
        import capo_groundstation.types.ephemeris_status

        out["status"] = capo_groundstation.types.ephemeris_status.deserialize_json(
            data["status"]
        )
    if "priority" in data:
        out["priority"] = data["priority"]
    if "creationTime" in data:
        import capo_groundstation.types._prelude.timestamp

        out["creation_time"] = (
            capo_groundstation.types._prelude.timestamp.deserialize_json(
                data["creationTime"]
            )
        )
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    if "name" in data:
        out["name"] = data["name"]
    if "tags" in data:
        import capo_groundstation.types.tags_map

        out["tags"] = capo_groundstation.types.tags_map.deserialize_json(data["tags"])
    if "suppliedData" in data:
        import capo_groundstation.types.ephemeris_type_description

        out["supplied_data"] = (
            capo_groundstation.types.ephemeris_type_description.deserialize_json(
                data["suppliedData"]
            )
        )
    if "invalidReason" in data:
        import capo_groundstation.types.ephemeris_invalid_reason

        out["invalid_reason"] = (
            capo_groundstation.types.ephemeris_invalid_reason.deserialize_json(
                data["invalidReason"]
            )
        )
    if "errorReasons" in data:
        import capo_groundstation.types.ephemeris_error_reason_list

        out["error_reasons"] = (
            capo_groundstation.types.ephemeris_error_reason_list.deserialize_json(
                data["errorReasons"]
            )
        )
    return out
