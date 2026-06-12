"""Generated from Smithy shape ``com.amazonaws.pi#ListPerformanceAnalysisReportsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_pi.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pi.types.boolean
    import aws_sdk_pi.types.identifier_string
    import aws_sdk_pi.types.max_results
    import aws_sdk_pi.types.next_token
    import aws_sdk_pi.types.service_type


class ListPerformanceAnalysisReportsRequest(TypedDict):
    service_type: "aws_sdk_pi.types.service_type.ServiceType"
    """<p>The Amazon Web Services service for which Performance Insights returns metrics. Valid value is <code>RDS</code>.</p>"""
    identifier: "aws_sdk_pi.types.identifier_string.IdentifierString"
    """<p>An immutable identifier for a data source that is unique for an Amazon Web Services Region. Performance Insights gathers metrics from this data source. In the console, the identifier is shown as <i>ResourceID</i>. When you call <code>DescribeDBInstances</code>, the identifier is returned as <code>DbiResourceId</code>.</p> <p>To use a DB instance as a data source, specify its <code>DbiResourceId</code> value. For example, specify <code>db-ABCDEFGHIJKLMNOPQRSTU1VW2X</code>.</p>"""
    next_token: NotRequired["aws_sdk_pi.types.next_token.NextToken"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the token, up to the value specified by <code>MaxResults</code>.</p>"""
    max_results: NotRequired["aws_sdk_pi.types.max_results.MaxResults"]
    """<p>The maximum number of items to return in the response. If more items exist than the specified <code>MaxResults</code> value, a pagination token is included in the response so that the remaining results can be retrieved. </p>"""
    list_tags: NotRequired["aws_sdk_pi.types.boolean.Boolean"]
    """<p>Specifies whether or not to include the list of tags in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPerformanceAnalysisReportsRequest) -> dict:
    out: dict = {}
    import aws_sdk_pi.types.service_type

    out["ServiceType"] = aws_sdk_pi.types.service_type.serialize_aws_json_1_1(
        value["service_type"]
    )
    out["Identifier"] = value["identifier"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "list_tags" in value:
        out["ListTags"] = value["list_tags"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPerformanceAnalysisReportsRequest:
    out: ListPerformanceAnalysisReportsRequest = {}  # type: ignore[typeddict-item]
    if "ServiceType" in data:
        import aws_sdk_pi.types.service_type

        out["service_type"] = aws_sdk_pi.types.service_type.deserialize_aws_json_1_1(
            data["ServiceType"]
        )
    else:
        raise DeserializationError(
            "ListPerformanceAnalysisReportsRequest.service_type required"
        )
    if "Identifier" in data:
        out["identifier"] = data["Identifier"]
    else:
        raise DeserializationError(
            "ListPerformanceAnalysisReportsRequest.identifier required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "ListTags" in data:
        out["list_tags"] = data["ListTags"]
    return out
