"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#StartQueryMonitorTopContributorsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_networkflowmonitor.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_networkflowmonitor.types.destination_category
    import aws_sdk_networkflowmonitor.types.limit
    import aws_sdk_networkflowmonitor.types.monitor_metric
    import aws_sdk_networkflowmonitor.types.resource_name


class StartQueryMonitorTopContributorsInput(TypedDict):
    monitor_name: "aws_sdk_networkflowmonitor.types.resource_name.ResourceName"
    """<p>The name of the monitor.</p>"""
    start_time: "datetime.datetime"
    """<p>The timestamp that is the date and time that is the beginning of the period that you want to retrieve results for with your query.</p>"""
    end_time: "datetime.datetime"
    """<p>The timestamp that is the date and time end of the period that you want to retrieve results for with your query.</p>"""
    metric_name: "aws_sdk_networkflowmonitor.types.monitor_metric.MonitorMetric"
    """<p>The metric that you want to query top contributors for. That is, you can specify a metric with this call and return the top contributor network flows, for that type of metric, for a monitor and (optionally) within a specific category, such as network flows between Availability Zones.</p>"""
    destination_category: (
        "aws_sdk_networkflowmonitor.types.destination_category.DestinationCategory"
    )
    """<p>The category that you want to query top contributors for, for a specific monitor. Destination categories can be one of the following: </p> <ul> <li> <p> <code>INTRA_AZ</code>: Top contributor network flows within a single Availability Zone</p> </li> <li> <p> <code>INTER_AZ</code>: Top contributor network flows between Availability Zones</p> </li> <li> <p> <code>INTER_REGION</code>: Top contributor network flows between Regions (to the edge of another Region)</p> </li> <li> <p> <code>INTER_VPC</code>: Top contributor network flows between VPCs</p> </li> <li> <p> <code>AMAZON_S3</code>: Top contributor network flows to or from Amazon S3</p> </li> <li> <p> <code>AMAZON_DYNAMODB</code>: Top contributor network flows to or from Amazon Dynamo DB</p> </li> <li> <p> <code>UNCLASSIFIED</code>: Top contributor network flows that do not have a bucket classification</p> </li> </ul>"""
    limit: NotRequired["aws_sdk_networkflowmonitor.types.limit.Limit"]
    """<p>The maximum number of top contributors to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartQueryMonitorTopContributorsInput) -> dict:
    out: dict = {}
    import aws_sdk_networkflowmonitor.types._prelude.timestamp

    out["startTime"] = (
        aws_sdk_networkflowmonitor.types._prelude.timestamp.serialize_json(
            value["start_time"]
        )
    )
    import aws_sdk_networkflowmonitor.types._prelude.timestamp

    out["endTime"] = aws_sdk_networkflowmonitor.types._prelude.timestamp.serialize_json(
        value["end_time"]
    )
    import aws_sdk_networkflowmonitor.types.monitor_metric

    out["metricName"] = aws_sdk_networkflowmonitor.types.monitor_metric.serialize_json(
        value["metric_name"]
    )
    import aws_sdk_networkflowmonitor.types.destination_category

    out["destinationCategory"] = (
        aws_sdk_networkflowmonitor.types.destination_category.serialize_json(
            value["destination_category"]
        )
    )
    if "limit" in value:
        out["limit"] = value["limit"]
    return out


def deserialize_json(data: dict) -> StartQueryMonitorTopContributorsInput:
    out: StartQueryMonitorTopContributorsInput = {}  # type: ignore[typeddict-item]
    if "startTime" in data:
        import aws_sdk_networkflowmonitor.types._prelude.timestamp

        out["start_time"] = (
            aws_sdk_networkflowmonitor.types._prelude.timestamp.deserialize_json(
                data["startTime"]
            )
        )
    else:
        raise DeserializationError(
            "StartQueryMonitorTopContributorsInput.start_time required"
        )
    if "endTime" in data:
        import aws_sdk_networkflowmonitor.types._prelude.timestamp

        out["end_time"] = (
            aws_sdk_networkflowmonitor.types._prelude.timestamp.deserialize_json(
                data["endTime"]
            )
        )
    else:
        raise DeserializationError(
            "StartQueryMonitorTopContributorsInput.end_time required"
        )
    if "metricName" in data:
        import aws_sdk_networkflowmonitor.types.monitor_metric

        out["metric_name"] = (
            aws_sdk_networkflowmonitor.types.monitor_metric.deserialize_json(
                data["metricName"]
            )
        )
    else:
        raise DeserializationError(
            "StartQueryMonitorTopContributorsInput.metric_name required"
        )
    if "destinationCategory" in data:
        import aws_sdk_networkflowmonitor.types.destination_category

        out["destination_category"] = (
            aws_sdk_networkflowmonitor.types.destination_category.deserialize_json(
                data["destinationCategory"]
            )
        )
    else:
        raise DeserializationError(
            "StartQueryMonitorTopContributorsInput.destination_category required"
        )
    if "limit" in data:
        out["limit"] = data["limit"]
    return out
