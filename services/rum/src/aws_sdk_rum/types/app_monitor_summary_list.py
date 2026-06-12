"""Generated from Smithy shape ``com.amazonaws.rum#AppMonitorSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_rum.types.app_monitor_summary

AppMonitorSummaryList: TypeAlias = list["aws_sdk_rum.types.app_monitor_summary.AppMonitorSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: AppMonitorSummaryList) -> list:
    import aws_sdk_rum.types.app_monitor_summary
    out: list = []
    for item in value:
        out.append(aws_sdk_rum.types.app_monitor_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> AppMonitorSummaryList:
    import aws_sdk_rum.types.app_monitor_summary
    out: AppMonitorSummaryList = []
    for item in data:
        out.append(aws_sdk_rum.types.app_monitor_summary.deserialize_json(item))
    return out