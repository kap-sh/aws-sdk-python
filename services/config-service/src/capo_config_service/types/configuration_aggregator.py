"""Generated from Smithy shape ``com.amazonaws.configservice#ConfigurationAggregator``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.account_aggregation_source_list
    import capo_config_service.types.aggregator_filters
    import capo_config_service.types.configuration_aggregator_arn
    import capo_config_service.types.configuration_aggregator_name
    import capo_config_service.types.date
    import capo_config_service.types.organization_aggregation_source
    import capo_config_service.types.string_with_char_limit256


class ConfigurationAggregator(TypedDict, closed=True):
    configuration_aggregator_name: NotRequired[
        "capo_config_service.types.configuration_aggregator_name.ConfigurationAggregatorName"
    ]
    """<p>The name of the aggregator.</p>"""
    configuration_aggregator_arn: NotRequired[
        "capo_config_service.types.configuration_aggregator_arn.ConfigurationAggregatorArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the aggregator.</p>"""
    account_aggregation_sources: NotRequired[
        "capo_config_service.types.account_aggregation_source_list.AccountAggregationSourceList"
    ]
    """<p>Provides a list of source accounts and regions to be aggregated.</p>"""
    organization_aggregation_source: NotRequired[
        "capo_config_service.types.organization_aggregation_source.OrganizationAggregationSource"
    ]
    """<p>Provides an organization and list of regions to be aggregated.</p>"""
    creation_time: NotRequired["capo_config_service.types.date.Date"]
    """<p>The time stamp when the configuration aggregator was created.</p>"""
    last_updated_time: NotRequired["capo_config_service.types.date.Date"]
    """<p>The time of the last update.</p>"""
    created_by: NotRequired[
        "capo_config_service.types.string_with_char_limit256.StringWithCharLimit256"
    ]
    """<p>Amazon Web Services service that created the configuration aggregator.</p>"""
    aggregator_filters: NotRequired[
        "capo_config_service.types.aggregator_filters.AggregatorFilters"
    ]
    """<p>An object to filter the data you specify for an aggregator.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigurationAggregator) -> dict:
    out: dict = {}
    if "configuration_aggregator_name" in value:
        out["ConfigurationAggregatorName"] = value["configuration_aggregator_name"]
    if "configuration_aggregator_arn" in value:
        out["ConfigurationAggregatorArn"] = value["configuration_aggregator_arn"]
    if "account_aggregation_sources" in value:
        import capo_config_service.types.account_aggregation_source_list

        out["AccountAggregationSources"] = (
            capo_config_service.types.account_aggregation_source_list.serialize_aws_json_1_1(
                value["account_aggregation_sources"]
            )
        )
    if "organization_aggregation_source" in value:
        import capo_config_service.types.organization_aggregation_source

        out["OrganizationAggregationSource"] = (
            capo_config_service.types.organization_aggregation_source.serialize_aws_json_1_1(
                value["organization_aggregation_source"]
            )
        )
    if "creation_time" in value:
        import capo_config_service.types.date

        out["CreationTime"] = capo_config_service.types.date.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_updated_time" in value:
        import capo_config_service.types.date

        out["LastUpdatedTime"] = capo_config_service.types.date.serialize_aws_json_1_1(
            value["last_updated_time"]
        )
    if "created_by" in value:
        out["CreatedBy"] = value["created_by"]
    if "aggregator_filters" in value:
        import capo_config_service.types.aggregator_filters

        out["AggregatorFilters"] = (
            capo_config_service.types.aggregator_filters.serialize_aws_json_1_1(
                value["aggregator_filters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConfigurationAggregator:
    out: ConfigurationAggregator = {}  # type: ignore[typeddict-item]
    if "ConfigurationAggregatorName" in data:
        out["configuration_aggregator_name"] = data["ConfigurationAggregatorName"]
    if "ConfigurationAggregatorArn" in data:
        out["configuration_aggregator_arn"] = data["ConfigurationAggregatorArn"]
    if "AccountAggregationSources" in data:
        import capo_config_service.types.account_aggregation_source_list

        out["account_aggregation_sources"] = (
            capo_config_service.types.account_aggregation_source_list.deserialize_aws_json_1_1(
                data["AccountAggregationSources"]
            )
        )
    if "OrganizationAggregationSource" in data:
        import capo_config_service.types.organization_aggregation_source

        out["organization_aggregation_source"] = (
            capo_config_service.types.organization_aggregation_source.deserialize_aws_json_1_1(
                data["OrganizationAggregationSource"]
            )
        )
    if "CreationTime" in data:
        import capo_config_service.types.date

        out["creation_time"] = capo_config_service.types.date.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if "LastUpdatedTime" in data:
        import capo_config_service.types.date

        out["last_updated_time"] = (
            capo_config_service.types.date.deserialize_aws_json_1_1(
                data["LastUpdatedTime"]
            )
        )
    if "CreatedBy" in data:
        out["created_by"] = data["CreatedBy"]
    if "AggregatorFilters" in data:
        import capo_config_service.types.aggregator_filters

        out["aggregator_filters"] = (
            capo_config_service.types.aggregator_filters.deserialize_aws_json_1_1(
                data["AggregatorFilters"]
            )
        )
    return out
