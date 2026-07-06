"""Generated from Smithy shape ``com.amazonaws.configservice#ListConfigurationRecordersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_config_service.types.configuration_recorder_filter_list
    import aws_sdk_config_service.types.max_results
    import aws_sdk_config_service.types.next_token


class ListConfigurationRecordersRequest(TypedDict, closed=True):
    filters: NotRequired[
        "aws_sdk_config_service.types.configuration_recorder_filter_list.ConfigurationRecorderFilterList"
    ]
    """<p>Filters the results based on a list of <code>ConfigurationRecorderFilter</code> objects that you specify.</p>"""
    max_results: NotRequired["aws_sdk_config_service.types.max_results.MaxResults"]
    """<p>The maximum number of results to include in the response.</p>"""
    next_token: NotRequired["aws_sdk_config_service.types.next_token.NextToken"]
    """<p>The <code>NextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListConfigurationRecordersRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import aws_sdk_config_service.types.configuration_recorder_filter_list

        out["Filters"] = (
            aws_sdk_config_service.types.configuration_recorder_filter_list.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListConfigurationRecordersRequest:
    out: ListConfigurationRecordersRequest = {}  # type: ignore[typeddict-item]
    if "Filters" in data:
        import aws_sdk_config_service.types.configuration_recorder_filter_list

        out["filters"] = (
            aws_sdk_config_service.types.configuration_recorder_filter_list.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
