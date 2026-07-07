"""Generated from Smithy shape ``com.amazonaws.drs#LifeCycle``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_drs.types.iso8601_datetime_string
    import aws_sdk_drs.types.iso8601_duration_string
    import aws_sdk_drs.types.life_cycle_last_launch


class LifeCycle(TypedDict, closed=True):
    added_to_service_date_time: NotRequired[
        "aws_sdk_drs.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>The date and time of when the Source Server was added to the service.</p>"""
    first_byte_date_time: NotRequired[
        "aws_sdk_drs.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>The date and time of the first byte that was replicated from the Source Server.</p>"""
    elapsed_replication_duration: NotRequired[
        "aws_sdk_drs.types.iso8601_duration_string.ISO8601DurationString"
    ]
    """<p>The amount of time that the Source Server has been replicating for.</p>"""
    last_seen_by_service_date_time: NotRequired[
        "aws_sdk_drs.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>The date and time this Source Server was last seen by the service.</p>"""
    last_launch: NotRequired[
        "aws_sdk_drs.types.life_cycle_last_launch.LifeCycleLastLaunch"
    ]
    """<p>An object containing information regarding the last launch of the Source Server.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LifeCycle) -> dict:
    out: dict = {}
    if "added_to_service_date_time" in value:
        out["addedToServiceDateTime"] = value["added_to_service_date_time"]
    if "first_byte_date_time" in value:
        out["firstByteDateTime"] = value["first_byte_date_time"]
    if "elapsed_replication_duration" in value:
        out["elapsedReplicationDuration"] = value["elapsed_replication_duration"]
    if "last_seen_by_service_date_time" in value:
        out["lastSeenByServiceDateTime"] = value["last_seen_by_service_date_time"]
    if "last_launch" in value:
        import aws_sdk_drs.types.life_cycle_last_launch

        out["lastLaunch"] = aws_sdk_drs.types.life_cycle_last_launch.serialize_json(
            value["last_launch"]
        )
    return out


def deserialize_json(data: dict) -> LifeCycle:
    out: LifeCycle = {}  # type: ignore[typeddict-item]
    if "addedToServiceDateTime" in data:
        out["added_to_service_date_time"] = data["addedToServiceDateTime"]
    if "firstByteDateTime" in data:
        out["first_byte_date_time"] = data["firstByteDateTime"]
    if "elapsedReplicationDuration" in data:
        out["elapsed_replication_duration"] = data["elapsedReplicationDuration"]
    if "lastSeenByServiceDateTime" in data:
        out["last_seen_by_service_date_time"] = data["lastSeenByServiceDateTime"]
    if "lastLaunch" in data:
        import aws_sdk_drs.types.life_cycle_last_launch

        out["last_launch"] = aws_sdk_drs.types.life_cycle_last_launch.deserialize_json(
            data["lastLaunch"]
        )
    return out
