"""Generated from Smithy shape ``com.amazonaws.detective#DatasourcePackageUsageInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_detective.types.byte_value
    import aws_sdk_detective.types.timestamp


class DatasourcePackageUsageInfo(TypedDict, closed=True):
    volume_usage_in_bytes: NotRequired["aws_sdk_detective.types.byte_value.ByteValue"]
    """<p>Total volume of data in bytes per day ingested for a given data source package.</p>"""
    volume_usage_update_time: NotRequired["aws_sdk_detective.types.timestamp.Timestamp"]
    """<p>The data and time when the member account data volume was last updated. The value is an ISO8601 formatted string. For example, <code>2021-08-18T16:35:56.284Z</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DatasourcePackageUsageInfo) -> dict:
    out: dict = {}
    if "volume_usage_in_bytes" in value:
        out["VolumeUsageInBytes"] = value["volume_usage_in_bytes"]
    if "volume_usage_update_time" in value:
        import aws_sdk_detective.types.timestamp

        out["VolumeUsageUpdateTime"] = aws_sdk_detective.types.timestamp.serialize_json(
            value["volume_usage_update_time"]
        )
    return out


def deserialize_json(data: dict) -> DatasourcePackageUsageInfo:
    out: DatasourcePackageUsageInfo = {}  # type: ignore[typeddict-item]
    if "VolumeUsageInBytes" in data:
        out["volume_usage_in_bytes"] = data["VolumeUsageInBytes"]
    if "VolumeUsageUpdateTime" in data:
        import aws_sdk_detective.types.timestamp

        out["volume_usage_update_time"] = (
            aws_sdk_detective.types.timestamp.deserialize_json(
                data["VolumeUsageUpdateTime"]
            )
        )
    return out
