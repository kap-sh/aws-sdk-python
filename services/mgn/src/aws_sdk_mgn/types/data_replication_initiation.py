"""Generated from Smithy shape ``com.amazonaws.mgn#DataReplicationInitiation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mgn.types.data_replication_initiation_steps
    import aws_sdk_mgn.types.iso8601_datetime_string


class DataReplicationInitiation(TypedDict, closed=True):
    start_date_time: NotRequired[
        "aws_sdk_mgn.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>Request to query data initiation start date and time.</p>"""
    next_attempt_date_time: NotRequired[
        "aws_sdk_mgn.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>Request to query next data initiation date and time.</p>"""
    steps: NotRequired[
        "aws_sdk_mgn.types.data_replication_initiation_steps.DataReplicationInitiationSteps"
    ]
    """<p>Request to query data initiation steps.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataReplicationInitiation) -> dict:
    out: dict = {}
    if "start_date_time" in value:
        out["startDateTime"] = value["start_date_time"]
    if "next_attempt_date_time" in value:
        out["nextAttemptDateTime"] = value["next_attempt_date_time"]
    if "steps" in value:
        import aws_sdk_mgn.types.data_replication_initiation_steps

        out["steps"] = (
            aws_sdk_mgn.types.data_replication_initiation_steps.serialize_json(
                value["steps"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataReplicationInitiation:
    out: DataReplicationInitiation = {}  # type: ignore[typeddict-item]
    if "startDateTime" in data:
        out["start_date_time"] = data["startDateTime"]
    if "nextAttemptDateTime" in data:
        out["next_attempt_date_time"] = data["nextAttemptDateTime"]
    if "steps" in data:
        import aws_sdk_mgn.types.data_replication_initiation_steps

        out["steps"] = (
            aws_sdk_mgn.types.data_replication_initiation_steps.deserialize_json(
                data["steps"]
            )
        )
    return out
