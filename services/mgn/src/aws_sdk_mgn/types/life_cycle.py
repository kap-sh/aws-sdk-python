"""Generated from Smithy shape ``com.amazonaws.mgn#LifeCycle``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mgn.types.iso8601_datetime_string
    import aws_sdk_mgn.types.iso8601_duration_string
    import aws_sdk_mgn.types.life_cycle_last_cutover
    import aws_sdk_mgn.types.life_cycle_last_test
    import aws_sdk_mgn.types.life_cycle_state


class LifeCycle(TypedDict, closed=True):
    added_to_service_date_time: NotRequired[
        "aws_sdk_mgn.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>Lifecycle added to service data and time.</p>"""
    first_byte_date_time: NotRequired[
        "aws_sdk_mgn.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>Lifecycle replication initiation date and time.</p>"""
    elapsed_replication_duration: NotRequired[
        "aws_sdk_mgn.types.iso8601_duration_string.ISO8601DurationString"
    ]
    """<p>Lifecycle elapsed time and duration.</p>"""
    last_seen_by_service_date_time: NotRequired[
        "aws_sdk_mgn.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>Lifecycle last seen date and time.</p>"""
    last_test: NotRequired["aws_sdk_mgn.types.life_cycle_last_test.LifeCycleLastTest"]
    """<p>Lifecycle last Test.</p>"""
    last_cutover: NotRequired[
        "aws_sdk_mgn.types.life_cycle_last_cutover.LifeCycleLastCutover"
    ]
    """<p>Lifecycle last Cutover.</p>"""
    state: NotRequired["aws_sdk_mgn.types.life_cycle_state.LifeCycleState"]
    """<p>Lifecycle state.</p>"""


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
    if "last_test" in value:
        import aws_sdk_mgn.types.life_cycle_last_test

        out["lastTest"] = aws_sdk_mgn.types.life_cycle_last_test.serialize_json(
            value["last_test"]
        )
    if "last_cutover" in value:
        import aws_sdk_mgn.types.life_cycle_last_cutover

        out["lastCutover"] = aws_sdk_mgn.types.life_cycle_last_cutover.serialize_json(
            value["last_cutover"]
        )
    if "state" in value:
        out["state"] = value["state"]
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
    if "lastTest" in data:
        import aws_sdk_mgn.types.life_cycle_last_test

        out["last_test"] = aws_sdk_mgn.types.life_cycle_last_test.deserialize_json(
            data["lastTest"]
        )
    if "lastCutover" in data:
        import aws_sdk_mgn.types.life_cycle_last_cutover

        out["last_cutover"] = (
            aws_sdk_mgn.types.life_cycle_last_cutover.deserialize_json(
                data["lastCutover"]
            )
        )
    if "state" in data:
        out["state"] = data["state"]
    return out
