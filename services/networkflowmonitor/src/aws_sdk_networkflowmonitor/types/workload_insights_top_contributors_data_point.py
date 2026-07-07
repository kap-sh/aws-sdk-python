"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#WorkloadInsightsTopContributorsDataPoint``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_networkflowmonitor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_networkflowmonitor.types.workload_insights_top_contributors_timestamps_list
    import aws_sdk_networkflowmonitor.types.workload_insights_top_contributors_values_list


class WorkloadInsightsTopContributorsDataPoint(TypedDict, closed=True):
    timestamps: "aws_sdk_networkflowmonitor.types.workload_insights_top_contributors_timestamps_list.WorkloadInsightsTopContributorsTimestampsList"
    """<p>An array of the timestamps for the data point.</p>"""
    values: "aws_sdk_networkflowmonitor.types.workload_insights_top_contributors_values_list.WorkloadInsightsTopContributorsValuesList"
    """<p>The values for the data point.</p>"""
    label: "str"
    """<p>The label identifying the data point.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkloadInsightsTopContributorsDataPoint) -> dict:
    out: dict = {}
    import aws_sdk_networkflowmonitor.types.workload_insights_top_contributors_timestamps_list

    out["timestamps"] = (
        aws_sdk_networkflowmonitor.types.workload_insights_top_contributors_timestamps_list.serialize_json(
            value["timestamps"]
        )
    )
    import aws_sdk_networkflowmonitor.types.workload_insights_top_contributors_values_list

    out["values"] = (
        aws_sdk_networkflowmonitor.types.workload_insights_top_contributors_values_list.serialize_json(
            value["values"]
        )
    )
    out["label"] = value["label"]
    return out


def deserialize_json(data: dict) -> WorkloadInsightsTopContributorsDataPoint:
    out: WorkloadInsightsTopContributorsDataPoint = {}  # type: ignore[typeddict-item]
    if "timestamps" in data:
        import aws_sdk_networkflowmonitor.types.workload_insights_top_contributors_timestamps_list

        out["timestamps"] = (
            aws_sdk_networkflowmonitor.types.workload_insights_top_contributors_timestamps_list.deserialize_json(
                data["timestamps"]
            )
        )
    else:
        raise DeserializationError(
            "WorkloadInsightsTopContributorsDataPoint.timestamps required"
        )
    if "values" in data:
        import aws_sdk_networkflowmonitor.types.workload_insights_top_contributors_values_list

        out["values"] = (
            aws_sdk_networkflowmonitor.types.workload_insights_top_contributors_values_list.deserialize_json(
                data["values"]
            )
        )
    else:
        raise DeserializationError(
            "WorkloadInsightsTopContributorsDataPoint.values required"
        )
    if "label" in data:
        out["label"] = data["label"]
    else:
        raise DeserializationError(
            "WorkloadInsightsTopContributorsDataPoint.label required"
        )
    return out
