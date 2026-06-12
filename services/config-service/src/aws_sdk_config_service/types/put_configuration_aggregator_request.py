"""Generated from Smithy shape ``com.amazonaws.configservice#PutConfigurationAggregatorRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.account_aggregation_source_list
    import aws_sdk_config_service.types.aggregator_filters
    import aws_sdk_config_service.types.configuration_aggregator_name
    import aws_sdk_config_service.types.organization_aggregation_source
    import aws_sdk_config_service.types.tags_list


class PutConfigurationAggregatorRequest(TypedDict):
    configuration_aggregator_name: "aws_sdk_config_service.types.configuration_aggregator_name.ConfigurationAggregatorName"
    """<p>The name of the configuration aggregator.</p>"""
    account_aggregation_sources: NotRequired[
        "aws_sdk_config_service.types.account_aggregation_source_list.AccountAggregationSourceList"
    ]
    """<p>A list of AccountAggregationSource object. </p>"""
    organization_aggregation_source: NotRequired[
        "aws_sdk_config_service.types.organization_aggregation_source.OrganizationAggregationSource"
    ]
    """<p>An OrganizationAggregationSource object.</p>"""
    tags: NotRequired["aws_sdk_config_service.types.tags_list.TagsList"]
    """<p>An array of tag object.</p>"""
    aggregator_filters: NotRequired[
        "aws_sdk_config_service.types.aggregator_filters.AggregatorFilters"
    ]
    """<p>An object to filter configuration recorders in an aggregator. Either <code>ResourceType</code> or <code>ServicePrincipal</code> is required.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutConfigurationAggregatorRequest) -> dict:
    out: dict = {}
    out["ConfigurationAggregatorName"] = value["configuration_aggregator_name"]
    if "account_aggregation_sources" in value:
        import aws_sdk_config_service.types.account_aggregation_source_list

        out["AccountAggregationSources"] = (
            aws_sdk_config_service.types.account_aggregation_source_list.serialize_aws_json_1_1(
                value["account_aggregation_sources"]
            )
        )
    if "organization_aggregation_source" in value:
        import aws_sdk_config_service.types.organization_aggregation_source

        out["OrganizationAggregationSource"] = (
            aws_sdk_config_service.types.organization_aggregation_source.serialize_aws_json_1_1(
                value["organization_aggregation_source"]
            )
        )
    if "tags" in value:
        import aws_sdk_config_service.types.tags_list

        out["Tags"] = aws_sdk_config_service.types.tags_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "aggregator_filters" in value:
        import aws_sdk_config_service.types.aggregator_filters

        out["AggregatorFilters"] = (
            aws_sdk_config_service.types.aggregator_filters.serialize_aws_json_1_1(
                value["aggregator_filters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutConfigurationAggregatorRequest:
    out: PutConfigurationAggregatorRequest = {}  # type: ignore[typeddict-item]
    if "ConfigurationAggregatorName" in data:
        out["configuration_aggregator_name"] = data["ConfigurationAggregatorName"]
    else:
        raise DeserializationError(
            "PutConfigurationAggregatorRequest.configuration_aggregator_name required"
        )
    if "AccountAggregationSources" in data:
        import aws_sdk_config_service.types.account_aggregation_source_list

        out["account_aggregation_sources"] = (
            aws_sdk_config_service.types.account_aggregation_source_list.deserialize_aws_json_1_1(
                data["AccountAggregationSources"]
            )
        )
    if "OrganizationAggregationSource" in data:
        import aws_sdk_config_service.types.organization_aggregation_source

        out["organization_aggregation_source"] = (
            aws_sdk_config_service.types.organization_aggregation_source.deserialize_aws_json_1_1(
                data["OrganizationAggregationSource"]
            )
        )
    if "Tags" in data:
        import aws_sdk_config_service.types.tags_list

        out["tags"] = aws_sdk_config_service.types.tags_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "AggregatorFilters" in data:
        import aws_sdk_config_service.types.aggregator_filters

        out["aggregator_filters"] = (
            aws_sdk_config_service.types.aggregator_filters.deserialize_aws_json_1_1(
                data["AggregatorFilters"]
            )
        )
    return out
