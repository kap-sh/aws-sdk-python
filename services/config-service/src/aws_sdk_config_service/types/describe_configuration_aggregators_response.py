"""Generated from Smithy shape ``com.amazonaws.configservice#DescribeConfigurationAggregatorsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_config_service.types.configuration_aggregator_list
    import aws_sdk_config_service.types.string


class DescribeConfigurationAggregatorsResponse(TypedDict, closed=True):
    configuration_aggregators: NotRequired[
        "aws_sdk_config_service.types.configuration_aggregator_list.ConfigurationAggregatorList"
    ]
    """<p>Returns a ConfigurationAggregators object.</p>"""
    next_token: NotRequired["aws_sdk_config_service.types.string.String"]
    """<p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeConfigurationAggregatorsResponse) -> dict:
    out: dict = {}
    if "configuration_aggregators" in value:
        import aws_sdk_config_service.types.configuration_aggregator_list

        out["ConfigurationAggregators"] = (
            aws_sdk_config_service.types.configuration_aggregator_list.serialize_aws_json_1_1(
                value["configuration_aggregators"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeConfigurationAggregatorsResponse:
    out: DescribeConfigurationAggregatorsResponse = {}  # type: ignore[typeddict-item]
    if "ConfigurationAggregators" in data:
        import aws_sdk_config_service.types.configuration_aggregator_list

        out["configuration_aggregators"] = (
            aws_sdk_config_service.types.configuration_aggregator_list.deserialize_aws_json_1_1(
                data["ConfigurationAggregators"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
