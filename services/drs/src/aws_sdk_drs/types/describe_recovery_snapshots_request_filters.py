"""Generated from Smithy shape ``com.amazonaws.drs#DescribeRecoverySnapshotsRequestFilters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_drs.types.iso8601_datetime_string


class DescribeRecoverySnapshotsRequestFilters(TypedDict):
    from_date_time: NotRequired[
        "aws_sdk_drs.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>The start date in a date range query.</p>"""
    to_date_time: NotRequired[
        "aws_sdk_drs.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>The end date in a date range query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeRecoverySnapshotsRequestFilters) -> dict:
    out: dict = {}
    if "from_date_time" in value:
        out["fromDateTime"] = value["from_date_time"]
    if "to_date_time" in value:
        out["toDateTime"] = value["to_date_time"]
    return out


def deserialize_json(data: dict) -> DescribeRecoverySnapshotsRequestFilters:
    out: DescribeRecoverySnapshotsRequestFilters = {}  # type: ignore[typeddict-item]
    if "fromDateTime" in data:
        out["from_date_time"] = data["fromDateTime"]
    if "toDateTime" in data:
        out["to_date_time"] = data["toDateTime"]
    return out
