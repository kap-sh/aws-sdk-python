"""Generated from Smithy shape ``com.amazonaws.configservice#GetAggregateConformancePackComplianceSummaryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.aggregate_conformance_pack_compliance_summary_filters
    import aws_sdk_config_service.types.aggregate_conformance_pack_compliance_summary_group_key
    import aws_sdk_config_service.types.configuration_aggregator_name
    import aws_sdk_config_service.types.limit
    import aws_sdk_config_service.types.next_token


class GetAggregateConformancePackComplianceSummaryRequest(TypedDict, closed=True):
    configuration_aggregator_name: "aws_sdk_config_service.types.configuration_aggregator_name.ConfigurationAggregatorName"
    """<p>The name of the configuration aggregator.</p>"""
    filters: NotRequired[
        "aws_sdk_config_service.types.aggregate_conformance_pack_compliance_summary_filters.AggregateConformancePackComplianceSummaryFilters"
    ]
    """<p>Filters the results based on the <code>AggregateConformancePackComplianceSummaryFilters</code> object.</p>"""
    group_by_key: NotRequired[
        "aws_sdk_config_service.types.aggregate_conformance_pack_compliance_summary_group_key.AggregateConformancePackComplianceSummaryGroupKey"
    ]
    """<p>Groups the result based on Amazon Web Services account ID or Amazon Web Services Region.</p>"""
    limit: "aws_sdk_config_service.types.limit.Limit"
    """<p>The maximum number of results returned on each page. The default is maximum. If you specify 0, Config uses the default.</p>"""
    next_token: NotRequired["aws_sdk_config_service.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: GetAggregateConformancePackComplianceSummaryRequest,
) -> dict:
    out: dict = {}
    out["ConfigurationAggregatorName"] = value["configuration_aggregator_name"]
    if "filters" in value:
        import aws_sdk_config_service.types.aggregate_conformance_pack_compliance_summary_filters

        out["Filters"] = (
            aws_sdk_config_service.types.aggregate_conformance_pack_compliance_summary_filters.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "group_by_key" in value:
        import aws_sdk_config_service.types.aggregate_conformance_pack_compliance_summary_group_key

        out["GroupByKey"] = (
            aws_sdk_config_service.types.aggregate_conformance_pack_compliance_summary_group_key.serialize_aws_json_1_1(
                value["group_by_key"]
            )
        )
    out["Limit"] = value.get("limit", 0)
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> GetAggregateConformancePackComplianceSummaryRequest:
    out: GetAggregateConformancePackComplianceSummaryRequest = {}  # type: ignore[typeddict-item]
    if "ConfigurationAggregatorName" in data:
        out["configuration_aggregator_name"] = data["ConfigurationAggregatorName"]
    else:
        raise DeserializationError(
            "GetAggregateConformancePackComplianceSummaryRequest.configuration_aggregator_name required"
        )
    if "Filters" in data:
        import aws_sdk_config_service.types.aggregate_conformance_pack_compliance_summary_filters

        out["filters"] = (
            aws_sdk_config_service.types.aggregate_conformance_pack_compliance_summary_filters.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if "GroupByKey" in data:
        import aws_sdk_config_service.types.aggregate_conformance_pack_compliance_summary_group_key

        out["group_by_key"] = (
            aws_sdk_config_service.types.aggregate_conformance_pack_compliance_summary_group_key.deserialize_aws_json_1_1(
                data["GroupByKey"]
            )
        )
    if "Limit" in data:
        out["limit"] = data["Limit"]
    else:
        out["limit"] = 0
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
