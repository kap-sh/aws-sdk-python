"""Generated from Smithy shape ``com.amazonaws.pi#ListAvailableResourceMetricsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_pi.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pi.types.identifier_string
    import aws_sdk_pi.types.max_results
    import aws_sdk_pi.types.metric_type_list
    import aws_sdk_pi.types.next_token
    import aws_sdk_pi.types.service_type


class ListAvailableResourceMetricsRequest(TypedDict, closed=True):
    service_type: "aws_sdk_pi.types.service_type.ServiceType"
    """<p>The Amazon Web Services service for which Performance Insights returns metrics.</p>"""
    identifier: "aws_sdk_pi.types.identifier_string.IdentifierString"
    """<p>An immutable identifier for a data source that is unique within an Amazon Web Services Region. Performance Insights gathers metrics from this data source. To use an Amazon RDS DB instance as a data source, specify its <code>DbiResourceId</code> value. For example, specify <code>db-ABCDEFGHIJKLMNOPQRSTU1VWZ</code>. </p>"""
    metric_types: "aws_sdk_pi.types.metric_type_list.MetricTypeList"
    """<p>The types of metrics to return in the response. Valid values in the array include the following:</p> <ul> <li> <p> <code>os</code> (OS counter metrics) - All engines</p> </li> <li> <p> <code>db</code> (DB load metrics) - All engines except for Amazon DocumentDB</p> </li> <li> <p> <code>db.sql.stats</code> (per-SQL metrics) - All engines except for Amazon DocumentDB</p> </li> <li> <p> <code>db.sql_tokenized.stats</code> (per-SQL digest metrics) - All engines except for Amazon DocumentDB</p> </li> </ul>"""
    next_token: NotRequired["aws_sdk_pi.types.next_token.NextToken"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the token, up to the value specified by <code>MaxRecords</code>. </p>"""
    max_results: NotRequired["aws_sdk_pi.types.max_results.MaxResults"]
    """<p>The maximum number of items to return. If the <code>MaxRecords</code> value is less than the number of existing items, the response includes a pagination token. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAvailableResourceMetricsRequest) -> dict:
    out: dict = {}
    import aws_sdk_pi.types.service_type

    out["ServiceType"] = aws_sdk_pi.types.service_type.serialize_aws_json_1_1(
        value["service_type"]
    )
    out["Identifier"] = value["identifier"]
    import aws_sdk_pi.types.metric_type_list

    out["MetricTypes"] = aws_sdk_pi.types.metric_type_list.serialize_aws_json_1_1(
        value["metric_types"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAvailableResourceMetricsRequest:
    out: ListAvailableResourceMetricsRequest = {}  # type: ignore[typeddict-item]
    if "ServiceType" in data:
        import aws_sdk_pi.types.service_type

        out["service_type"] = aws_sdk_pi.types.service_type.deserialize_aws_json_1_1(
            data["ServiceType"]
        )
    else:
        raise DeserializationError(
            "ListAvailableResourceMetricsRequest.service_type required"
        )
    if "Identifier" in data:
        out["identifier"] = data["Identifier"]
    else:
        raise DeserializationError(
            "ListAvailableResourceMetricsRequest.identifier required"
        )
    if "MetricTypes" in data:
        import aws_sdk_pi.types.metric_type_list

        out["metric_types"] = (
            aws_sdk_pi.types.metric_type_list.deserialize_aws_json_1_1(
                data["MetricTypes"]
            )
        )
    else:
        raise DeserializationError(
            "ListAvailableResourceMetricsRequest.metric_types required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
