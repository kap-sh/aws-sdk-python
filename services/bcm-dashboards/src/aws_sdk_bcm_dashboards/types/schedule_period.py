"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#SchedulePeriod``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bcm_dashboards.types.generic_time_stamp


class SchedulePeriod(TypedDict, closed=True):
    start_time: NotRequired[
        "aws_sdk_bcm_dashboards.types.generic_time_stamp.GenericTimeStamp"
    ]
    """<p>The start time of the schedule period. If not specified, defaults to the time of the create or update request. The start time cannot be more than 5 minutes before the time of the request.</p>"""
    end_time: NotRequired[
        "aws_sdk_bcm_dashboards.types.generic_time_stamp.GenericTimeStamp"
    ]
    """<p>The end time of the schedule period. If not specified, defaults to 3 years from the time of the create or update request. The maximum allowed value is 3 years from the current time. Setting an end time beyond this limit returns a <code>ValidationException</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SchedulePeriod) -> dict:
    out: dict = {}
    if "start_time" in value:
        import aws_sdk_bcm_dashboards.types.generic_time_stamp

        out["startTime"] = (
            aws_sdk_bcm_dashboards.types.generic_time_stamp.serialize_aws_json_1_0(
                value["start_time"]
            )
        )
    if "end_time" in value:
        import aws_sdk_bcm_dashboards.types.generic_time_stamp

        out["endTime"] = (
            aws_sdk_bcm_dashboards.types.generic_time_stamp.serialize_aws_json_1_0(
                value["end_time"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> SchedulePeriod:
    out: SchedulePeriod = {}  # type: ignore[typeddict-item]
    if "startTime" in data:
        import aws_sdk_bcm_dashboards.types.generic_time_stamp

        out["start_time"] = (
            aws_sdk_bcm_dashboards.types.generic_time_stamp.deserialize_aws_json_1_0(
                data["startTime"]
            )
        )
    if "endTime" in data:
        import aws_sdk_bcm_dashboards.types.generic_time_stamp

        out["end_time"] = (
            aws_sdk_bcm_dashboards.types.generic_time_stamp.deserialize_aws_json_1_0(
                data["endTime"]
            )
        )
    return out
