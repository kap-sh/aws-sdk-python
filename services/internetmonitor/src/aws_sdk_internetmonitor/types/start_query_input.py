"""Generated from Smithy shape ``com.amazonaws.internetmonitor#StartQueryInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_internetmonitor.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_internetmonitor.types.account_id
    import aws_sdk_internetmonitor.types.filter_parameters
    import aws_sdk_internetmonitor.types.query_type
    import aws_sdk_internetmonitor.types.resource_name


class StartQueryInput(TypedDict):
    monitor_name: "aws_sdk_internetmonitor.types.resource_name.ResourceName"
    """<p>The name of the monitor to query.</p>"""
    start_time: "datetime.datetime"
    """<p>The timestamp that is the beginning of the period that you want to retrieve data for with your query.</p>"""
    end_time: "datetime.datetime"
    """<p>The timestamp that is the end of the period that you want to retrieve data for with your query.</p>"""
    query_type: "aws_sdk_internetmonitor.types.query_type.QueryType"
    r"""<p>The type of query to run. The following are the three types of queries that you can run using the Internet Monitor query interface:</p> <ul> <li> <p> <code>MEASUREMENTS</code>: Provides availability score, performance score, total traffic, and round-trip times, at 5 minute intervals.</p> </li> <li> <p> <code>TOP_LOCATIONS</code>: Provides availability score, performance score, total traffic, and time to first byte (TTFB) information, for the top location and ASN combinations that you're monitoring, by traffic volume.</p> </li> <li> <p> <code>TOP_LOCATION_DETAILS</code>: Provides TTFB for Amazon CloudFront, your current configuration, and the best performing EC2 configuration, at 1 hour intervals.</p> </li> <li> <p> <code>OVERALL_TRAFFIC_SUGGESTIONS</code>: Provides TTFB, using a 30-day weighted average, for all traffic in each Amazon Web Services location that is monitored.</p> </li> <li> <p> <code>OVERALL_TRAFFIC_SUGGESTIONS_DETAILS</code>: Provides TTFB, using a 30-day weighted average, for each top location, for a proposed Amazon Web Services location. Must provide an Amazon Web Services location to search.</p> </li> <li> <p> <code>ROUTING_SUGGESTIONS</code>: Provides the predicted average round-trip time (RTT) from an IP prefix toward an Amazon Web Services location for a DNS resolver. The RTT is calculated at one hour intervals, over a one hour period.</p> </li> </ul> <p>For lists of the fields returned with each query type and more information about how each type of query is performed, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-view-cw-tools-cwim-query.html\"> Using the Amazon CloudWatch Internet Monitor query interface</a> in the Amazon CloudWatch Internet Monitor User Guide.</p>"""
    filter_parameters: NotRequired[
        "aws_sdk_internetmonitor.types.filter_parameters.FilterParameters"
    ]
    r"""<p>The <code>FilterParameters</code> field that you use with Amazon CloudWatch Internet Monitor queries is a string the defines how you want a query to be filtered. The filter parameters that you can specify depend on the query type, since each query type returns a different set of Internet Monitor data.</p> <p>For more information about specifying filter parameters, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-view-cw-tools-cwim-query.html\">Using the Amazon CloudWatch Internet Monitor query interface</a> in the Amazon CloudWatch Internet Monitor User Guide.</p>"""
    linked_account_id: NotRequired["aws_sdk_internetmonitor.types.account_id.AccountId"]
    r"""<p>The account ID for an account that you've set up cross-account sharing for in Amazon CloudWatch Internet Monitor. You configure cross-account sharing by using Amazon CloudWatch Observability Access Manager. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cwim-cross-account.html\">Internet Monitor cross-account observability</a> in the Amazon CloudWatch Internet Monitor User Guide.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartQueryInput) -> dict:
    out: dict = {}
    import aws_sdk_internetmonitor.types._prelude.timestamp

    out["StartTime"] = aws_sdk_internetmonitor.types._prelude.timestamp.serialize_json(
        value["start_time"]
    )
    import aws_sdk_internetmonitor.types._prelude.timestamp

    out["EndTime"] = aws_sdk_internetmonitor.types._prelude.timestamp.serialize_json(
        value["end_time"]
    )
    out["QueryType"] = value["query_type"]
    if "filter_parameters" in value:
        import aws_sdk_internetmonitor.types.filter_parameters

        out["FilterParameters"] = (
            aws_sdk_internetmonitor.types.filter_parameters.serialize_json(
                value["filter_parameters"]
            )
        )
    if "linked_account_id" in value:
        out["LinkedAccountId"] = value["linked_account_id"]
    return out


def deserialize_json(data: dict) -> StartQueryInput:
    out: StartQueryInput = {}  # type: ignore[typeddict-item]
    if "StartTime" in data:
        import aws_sdk_internetmonitor.types._prelude.timestamp

        out["start_time"] = (
            aws_sdk_internetmonitor.types._prelude.timestamp.deserialize_json(
                data["StartTime"]
            )
        )
    else:
        raise DeserializationError("StartQueryInput.start_time required")
    if "EndTime" in data:
        import aws_sdk_internetmonitor.types._prelude.timestamp

        out["end_time"] = (
            aws_sdk_internetmonitor.types._prelude.timestamp.deserialize_json(
                data["EndTime"]
            )
        )
    else:
        raise DeserializationError("StartQueryInput.end_time required")
    if "QueryType" in data:
        out["query_type"] = data["QueryType"]
    else:
        raise DeserializationError("StartQueryInput.query_type required")
    if "FilterParameters" in data:
        import aws_sdk_internetmonitor.types.filter_parameters

        out["filter_parameters"] = (
            aws_sdk_internetmonitor.types.filter_parameters.deserialize_json(
                data["FilterParameters"]
            )
        )
    if "LinkedAccountId" in data:
        out["linked_account_id"] = data["LinkedAccountId"]
    return out
