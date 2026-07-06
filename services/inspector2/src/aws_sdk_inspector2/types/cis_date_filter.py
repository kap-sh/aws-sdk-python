"""Generated from Smithy shape ``com.amazonaws.inspector2#CisDateFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime


class CisDateFilter(TypedDict, closed=True):
    earliest_scan_start_time: NotRequired["datetime.datetime"]
    """<p>The CIS date filter's earliest scan start time.</p>"""
    latest_scan_start_time: NotRequired["datetime.datetime"]
    """<p>The CIS date filter's latest scan start time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CisDateFilter) -> dict:
    out: dict = {}
    if "earliest_scan_start_time" in value:
        import aws_sdk_inspector2.types._prelude.timestamp

        out["earliestScanStartTime"] = (
            aws_sdk_inspector2.types._prelude.timestamp.serialize_json(
                value["earliest_scan_start_time"]
            )
        )
    if "latest_scan_start_time" in value:
        import aws_sdk_inspector2.types._prelude.timestamp

        out["latestScanStartTime"] = (
            aws_sdk_inspector2.types._prelude.timestamp.serialize_json(
                value["latest_scan_start_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> CisDateFilter:
    out: CisDateFilter = {}  # type: ignore[typeddict-item]
    if "earliestScanStartTime" in data:
        import aws_sdk_inspector2.types._prelude.timestamp

        out["earliest_scan_start_time"] = (
            aws_sdk_inspector2.types._prelude.timestamp.deserialize_json(
                data["earliestScanStartTime"]
            )
        )
    if "latestScanStartTime" in data:
        import aws_sdk_inspector2.types._prelude.timestamp

        out["latest_scan_start_time"] = (
            aws_sdk_inspector2.types._prelude.timestamp.deserialize_json(
                data["latestScanStartTime"]
            )
        )
    return out
