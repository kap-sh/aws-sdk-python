"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#StartQueryWorkloadInsightsTopContributorsDataInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_networkflowmonitor.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_networkflowmonitor.types.destination_category
    import aws_sdk_networkflowmonitor.types.scope_id
    import aws_sdk_networkflowmonitor.types.workload_insights_metric


class StartQueryWorkloadInsightsTopContributorsDataInput(TypedDict, closed=True):
    scope_id: "aws_sdk_networkflowmonitor.types.scope_id.ScopeId"
    """<p>The identifier for the scope that includes the resources you want to get data results for. A scope ID is an internally-generated identifier that includes all the resources for a specific root account.</p>"""
    start_time: "datetime.datetime"
    """<p>The timestamp that is the date and time that is the beginning of the period that you want to retrieve results for with your query.</p>"""
    end_time: "datetime.datetime"
    """<p>The timestamp that is the date and time end of the period that you want to retrieve results for with your query.</p>"""
    metric_name: "aws_sdk_networkflowmonitor.types.workload_insights_metric.WorkloadInsightsMetric"
    """<p>The metric that you want to query top contributors for. That is, you can specify this metric to return the top contributor network flows, for this type of metric, for a monitor and (optionally) within a specific category, such as network flows between Availability Zones.</p>"""
    destination_category: (
        "aws_sdk_networkflowmonitor.types.destination_category.DestinationCategory"
    )
    """<p>The destination category for a top contributors. Destination categories can be one of the following: </p> <ul> <li> <p> <code>INTRA_AZ</code>: Top contributor network flows within a single Availability Zone</p> </li> <li> <p> <code>INTER_AZ</code>: Top contributor network flows between Availability Zones</p> </li> <li> <p> <code>INTER_REGION</code>: Top contributor network flows between Regions (to the edge of another Region)</p> </li> <li> <p> <code>INTER_VPC</code>: Top contributor network flows between VPCs</p> </li> <li> <p> <code>AWS_SERVICES</code>: Top contributor network flows to or from Amazon Web Services services</p> </li> <li> <p> <code>UNCLASSIFIED</code>: Top contributor network flows that do not have a bucket classification</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartQueryWorkloadInsightsTopContributorsDataInput) -> dict:
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
    import aws_sdk_networkflowmonitor.types.workload_insights_metric

    out["metricName"] = (
        aws_sdk_networkflowmonitor.types.workload_insights_metric.serialize_json(
            value["metric_name"]
        )
    )
    import aws_sdk_networkflowmonitor.types.destination_category

    out["destinationCategory"] = (
        aws_sdk_networkflowmonitor.types.destination_category.serialize_json(
            value["destination_category"]
        )
    )
    return out


def deserialize_json(data: dict) -> StartQueryWorkloadInsightsTopContributorsDataInput:
    out: StartQueryWorkloadInsightsTopContributorsDataInput = {}  # type: ignore[typeddict-item]
    if "startTime" in data:
        import aws_sdk_networkflowmonitor.types._prelude.timestamp

        out["start_time"] = (
            aws_sdk_networkflowmonitor.types._prelude.timestamp.deserialize_json(
                data["startTime"]
            )
        )
    else:
        raise DeserializationError(
            "StartQueryWorkloadInsightsTopContributorsDataInput.start_time required"
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
            "StartQueryWorkloadInsightsTopContributorsDataInput.end_time required"
        )
    if "metricName" in data:
        import aws_sdk_networkflowmonitor.types.workload_insights_metric

        out["metric_name"] = (
            aws_sdk_networkflowmonitor.types.workload_insights_metric.deserialize_json(
                data["metricName"]
            )
        )
    else:
        raise DeserializationError(
            "StartQueryWorkloadInsightsTopContributorsDataInput.metric_name required"
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
            "StartQueryWorkloadInsightsTopContributorsDataInput.destination_category required"
        )
    return out
