"""Generated from Smithy shape ``com.amazonaws.configservice#DescribeConfigurationAggregatorsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_config_service.types.configuration_aggregator_name_list
    import aws_sdk_config_service.types.limit
    import aws_sdk_config_service.types.string


class DescribeConfigurationAggregatorsRequest(TypedDict):
    configuration_aggregator_names: NotRequired[
        "aws_sdk_config_service.types.configuration_aggregator_name_list.ConfigurationAggregatorNameList"
    ]
    """<p>The name of the configuration aggregators.</p>"""
    next_token: NotRequired["aws_sdk_config_service.types.string.String"]
    """<p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>"""
    limit: "aws_sdk_config_service.types.limit.Limit"
    """<p>The maximum number of configuration aggregators returned on each page. The default is maximum. If you specify 0, Config uses the default.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeConfigurationAggregatorsRequest) -> dict:
    out: dict = {}
    if "configuration_aggregator_names" in value:
        import aws_sdk_config_service.types.configuration_aggregator_name_list

        out["ConfigurationAggregatorNames"] = (
            aws_sdk_config_service.types.configuration_aggregator_name_list.serialize_aws_json_1_1(
                value["configuration_aggregator_names"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    out["Limit"] = value.get("limit", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeConfigurationAggregatorsRequest:
    out: DescribeConfigurationAggregatorsRequest = {}  # type: ignore[typeddict-item]
    if "ConfigurationAggregatorNames" in data:
        import aws_sdk_config_service.types.configuration_aggregator_name_list

        out["configuration_aggregator_names"] = (
            aws_sdk_config_service.types.configuration_aggregator_name_list.deserialize_aws_json_1_1(
                data["ConfigurationAggregatorNames"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Limit" in data:
        out["limit"] = data["Limit"]
    else:
        out["limit"] = 0
    return out
