"""Generated from Smithy shape ``com.amazonaws.devopsguru#CloudWatchMetricsDataSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.cloud_watch_metric_data_status_code
    import capo_devops_guru.types.timestamp_metric_value_pair_list


class CloudWatchMetricsDataSummary(TypedDict, closed=True):
    timestamp_metric_value_pair_list: NotRequired[
        "capo_devops_guru.types.timestamp_metric_value_pair_list.TimestampMetricValuePairList"
    ]
    """<p>This is a list of Amazon CloudWatch metric values at given timestamp.</p>"""
    status_code: NotRequired[
        "capo_devops_guru.types.cloud_watch_metric_data_status_code.CloudWatchMetricDataStatusCode"
    ]
    """<p>This is an enum of the status showing whether the metric value pair list has partial or complete data, or if there was an error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudWatchMetricsDataSummary) -> dict:
    out: dict = {}
    if "timestamp_metric_value_pair_list" in value:
        import capo_devops_guru.types.timestamp_metric_value_pair_list

        out["TimestampMetricValuePairList"] = (
            capo_devops_guru.types.timestamp_metric_value_pair_list.serialize_json(
                value["timestamp_metric_value_pair_list"]
            )
        )
    if "status_code" in value:
        import capo_devops_guru.types.cloud_watch_metric_data_status_code

        out["StatusCode"] = (
            capo_devops_guru.types.cloud_watch_metric_data_status_code.serialize_json(
                value["status_code"]
            )
        )
    return out


def deserialize_json(data: dict) -> CloudWatchMetricsDataSummary:
    out: CloudWatchMetricsDataSummary = {}  # type: ignore[typeddict-item]
    if "TimestampMetricValuePairList" in data:
        import capo_devops_guru.types.timestamp_metric_value_pair_list

        out["timestamp_metric_value_pair_list"] = (
            capo_devops_guru.types.timestamp_metric_value_pair_list.deserialize_json(
                data["TimestampMetricValuePairList"]
            )
        )
    if "StatusCode" in data:
        import capo_devops_guru.types.cloud_watch_metric_data_status_code

        out["status_code"] = (
            capo_devops_guru.types.cloud_watch_metric_data_status_code.deserialize_json(
                data["StatusCode"]
            )
        )
    return out
