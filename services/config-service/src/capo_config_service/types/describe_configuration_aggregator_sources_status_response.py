"""Generated from Smithy shape ``com.amazonaws.configservice#DescribeConfigurationAggregatorSourcesStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.aggregated_source_status_list
    import capo_config_service.types.string


class DescribeConfigurationAggregatorSourcesStatusResponse(TypedDict, closed=True):
    aggregated_source_status_list: NotRequired[
        "capo_config_service.types.aggregated_source_status_list.AggregatedSourceStatusList"
    ]
    """<p>Returns an AggregatedSourceStatus object. </p>"""
    next_token: NotRequired["capo_config_service.types.string.String"]
    """<p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeConfigurationAggregatorSourcesStatusResponse,
) -> dict:
    out: dict = {}
    if "aggregated_source_status_list" in value:
        import capo_config_service.types.aggregated_source_status_list

        out["AggregatedSourceStatusList"] = (
            capo_config_service.types.aggregated_source_status_list.serialize_aws_json_1_1(
                value["aggregated_source_status_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeConfigurationAggregatorSourcesStatusResponse:
    out: DescribeConfigurationAggregatorSourcesStatusResponse = {}  # type: ignore[typeddict-item]
    if "AggregatedSourceStatusList" in data:
        import capo_config_service.types.aggregated_source_status_list

        out["aggregated_source_status_list"] = (
            capo_config_service.types.aggregated_source_status_list.deserialize_aws_json_1_1(
                data["AggregatedSourceStatusList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
