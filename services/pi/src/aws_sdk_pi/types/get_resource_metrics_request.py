"""Generated from Smithy shape ``com.amazonaws.pi#GetResourceMetricsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_pi.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pi.types.identifier_string
    import aws_sdk_pi.types.integer
    import aws_sdk_pi.types.iso_timestamp
    import aws_sdk_pi.types.max_results
    import aws_sdk_pi.types.metric_query_list
    import aws_sdk_pi.types.next_token
    import aws_sdk_pi.types.period_alignment
    import aws_sdk_pi.types.service_type


class GetResourceMetricsRequest(TypedDict):
    service_type: "aws_sdk_pi.types.service_type.ServiceType"
    """<p>The Amazon Web Services service for which Performance Insights returns metrics. Valid values are as follows:</p> <ul> <li> <p> <code>RDS</code> </p> </li> <li> <p> <code>DOCDB</code> </p> </li> </ul>"""
    identifier: "aws_sdk_pi.types.identifier_string.IdentifierString"
    """<p>An immutable identifier for a data source that is unique for an Amazon Web Services Region. Performance Insights gathers metrics from this data source. In the console, the identifier is shown as <i>ResourceID</i>. When you call <code>DescribeDBInstances</code>, the identifier is returned as <code>DbiResourceId</code>.</p> <p>To use a DB instance as a data source, specify its <code>DbiResourceId</code> value. For example, specify <code>db-ABCDEFGHIJKLMNOPQRSTU1VW2X</code>.</p>"""
    metric_queries: "aws_sdk_pi.types.metric_query_list.MetricQueryList"
    """<p>An array of one or more queries to perform. Each query must specify a Performance Insights metric and specify an aggregate function, and you can provide filtering criteria. You must append the aggregate function to the metric. For example, to find the average for the metric <code>db.load</code> you must use <code>db.load.avg</code>. Valid values for aggregate functions include <code>.avg</code>, <code>.min</code>, <code>.max</code>, and <code>.sum</code>.</p>"""
    start_time: "aws_sdk_pi.types.iso_timestamp.ISOTimestamp"
    """<p>The date and time specifying the beginning of the requested time series query range. You can't specify a <code>StartTime</code> that is earlier than 7 days ago. By default, Performance Insights has 7 days of retention, but you can extend this range up to 2 years. The value specified is <i>inclusive</i>. Thus, the command returns data points equal to or greater than <code>StartTime</code>.</p> <p>The value for <code>StartTime</code> must be earlier than the value for <code>EndTime</code>.</p>"""
    end_time: "aws_sdk_pi.types.iso_timestamp.ISOTimestamp"
    """<p>The date and time specifying the end of the requested time series query range. The value specified is <i>exclusive</i>. Thus, the command returns data points less than (but not equal to) <code>EndTime</code>.</p> <p>The value for <code>EndTime</code> must be later than the value for <code>StartTime</code>.</p>"""
    period_in_seconds: NotRequired["aws_sdk_pi.types.integer.Integer"]
    """<p>The granularity, in seconds, of the data points returned from Performance Insights. A period can be as short as one second, or as long as one day (86400 seconds). Valid values are:</p> <ul> <li> <p> <code>1</code> (one second)</p> </li> <li> <p> <code>60</code> (one minute)</p> </li> <li> <p> <code>300</code> (five minutes)</p> </li> <li> <p> <code>3600</code> (one hour)</p> </li> <li> <p> <code>86400</code> (twenty-four hours)</p> </li> </ul> <p>If you don't specify <code>PeriodInSeconds</code>, then Performance Insights will choose a value for you, with a goal of returning roughly 100-200 data points in the response.</p>"""
    max_results: NotRequired["aws_sdk_pi.types.max_results.MaxResults"]
    """<p>The maximum number of items to return in the response.</p>"""
    next_token: NotRequired["aws_sdk_pi.types.next_token.NextToken"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the token, up to the value specified by <code>MaxRecords</code>.</p>"""
    period_alignment: NotRequired["aws_sdk_pi.types.period_alignment.PeriodAlignment"]
    """<p>The returned timestamp which is the start or end time of the time periods. The default value is <code>END_TIME</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetResourceMetricsRequest) -> dict:
    out: dict = {}
    import aws_sdk_pi.types.service_type

    out["ServiceType"] = aws_sdk_pi.types.service_type.serialize_aws_json_1_1(
        value["service_type"]
    )
    out["Identifier"] = value["identifier"]
    import aws_sdk_pi.types.metric_query_list

    out["MetricQueries"] = aws_sdk_pi.types.metric_query_list.serialize_aws_json_1_1(
        value["metric_queries"]
    )
    import aws_sdk_pi.types.iso_timestamp

    out["StartTime"] = aws_sdk_pi.types.iso_timestamp.serialize_aws_json_1_1(
        value["start_time"]
    )
    import aws_sdk_pi.types.iso_timestamp

    out["EndTime"] = aws_sdk_pi.types.iso_timestamp.serialize_aws_json_1_1(
        value["end_time"]
    )
    if "period_in_seconds" in value:
        out["PeriodInSeconds"] = value["period_in_seconds"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "period_alignment" in value:
        import aws_sdk_pi.types.period_alignment

        out["PeriodAlignment"] = (
            aws_sdk_pi.types.period_alignment.serialize_aws_json_1_1(
                value["period_alignment"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetResourceMetricsRequest:
    out: GetResourceMetricsRequest = {}  # type: ignore[typeddict-item]
    if "ServiceType" in data:
        import aws_sdk_pi.types.service_type

        out["service_type"] = aws_sdk_pi.types.service_type.deserialize_aws_json_1_1(
            data["ServiceType"]
        )
    else:
        raise DeserializationError("GetResourceMetricsRequest.service_type required")
    if "Identifier" in data:
        out["identifier"] = data["Identifier"]
    else:
        raise DeserializationError("GetResourceMetricsRequest.identifier required")
    if "MetricQueries" in data:
        import aws_sdk_pi.types.metric_query_list

        out["metric_queries"] = (
            aws_sdk_pi.types.metric_query_list.deserialize_aws_json_1_1(
                data["MetricQueries"]
            )
        )
    else:
        raise DeserializationError("GetResourceMetricsRequest.metric_queries required")
    if "StartTime" in data:
        import aws_sdk_pi.types.iso_timestamp

        out["start_time"] = aws_sdk_pi.types.iso_timestamp.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    else:
        raise DeserializationError("GetResourceMetricsRequest.start_time required")
    if "EndTime" in data:
        import aws_sdk_pi.types.iso_timestamp

        out["end_time"] = aws_sdk_pi.types.iso_timestamp.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    else:
        raise DeserializationError("GetResourceMetricsRequest.end_time required")
    if "PeriodInSeconds" in data:
        out["period_in_seconds"] = data["PeriodInSeconds"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "PeriodAlignment" in data:
        import aws_sdk_pi.types.period_alignment

        out["period_alignment"] = (
            aws_sdk_pi.types.period_alignment.deserialize_aws_json_1_1(
                data["PeriodAlignment"]
            )
        )
    return out
