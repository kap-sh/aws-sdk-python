"""Generated from Smithy shape ``com.amazonaws.configservice#ListConfigurationRecordersResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.configuration_recorder_summaries
    import aws_sdk_config_service.types.next_token


class ListConfigurationRecordersResponse(TypedDict):
    configuration_recorder_summaries: "aws_sdk_config_service.types.configuration_recorder_summaries.ConfigurationRecorderSummaries"
    """<p>A list of <code>ConfigurationRecorderSummary</code> objects that includes.</p>"""
    next_token: NotRequired["aws_sdk_config_service.types.next_token.NextToken"]
    """<p>The <code>NextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListConfigurationRecordersResponse) -> dict:
    out: dict = {}
    import aws_sdk_config_service.types.configuration_recorder_summaries

    out["ConfigurationRecorderSummaries"] = (
        aws_sdk_config_service.types.configuration_recorder_summaries.serialize_aws_json_1_1(
            value["configuration_recorder_summaries"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListConfigurationRecordersResponse:
    out: ListConfigurationRecordersResponse = {}  # type: ignore[typeddict-item]
    if "ConfigurationRecorderSummaries" in data:
        import aws_sdk_config_service.types.configuration_recorder_summaries

        out["configuration_recorder_summaries"] = (
            aws_sdk_config_service.types.configuration_recorder_summaries.deserialize_aws_json_1_1(
                data["ConfigurationRecorderSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListConfigurationRecordersResponse.configuration_recorder_summaries required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
