"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#DateTimeRange``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bcm_dashboards.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bcm_dashboards.types.date_time_value


class DateTimeRange(TypedDict, closed=True):
    start_time: "capo_bcm_dashboards.types.date_time_value.DateTimeValue"
    """<p>The start time of the date range for querying data.</p>"""
    end_time: "capo_bcm_dashboards.types.date_time_value.DateTimeValue"
    """<p>The end time of the date range for querying data.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DateTimeRange) -> dict:
    out: dict = {}
    import capo_bcm_dashboards.types.date_time_value

    out["startTime"] = capo_bcm_dashboards.types.date_time_value.serialize_aws_json_1_0(
        value["start_time"]
    )
    import capo_bcm_dashboards.types.date_time_value

    out["endTime"] = capo_bcm_dashboards.types.date_time_value.serialize_aws_json_1_0(
        value["end_time"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DateTimeRange:
    out: DateTimeRange = {}  # type: ignore[typeddict-item]
    if "startTime" in data:
        import capo_bcm_dashboards.types.date_time_value

        out["start_time"] = (
            capo_bcm_dashboards.types.date_time_value.deserialize_aws_json_1_0(
                data["startTime"]
            )
        )
    else:
        raise DeserializationError("DateTimeRange.start_time required")
    if "endTime" in data:
        import capo_bcm_dashboards.types.date_time_value

        out["end_time"] = (
            capo_bcm_dashboards.types.date_time_value.deserialize_aws_json_1_0(
                data["endTime"]
            )
        )
    else:
        raise DeserializationError("DateTimeRange.end_time required")
    return out
