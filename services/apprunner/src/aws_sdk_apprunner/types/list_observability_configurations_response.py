"""Generated from Smithy shape ``com.amazonaws.apprunner#ListObservabilityConfigurationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_apprunner.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.next_token
    import aws_sdk_apprunner.types.observability_configuration_summary_list


class ListObservabilityConfigurationsResponse(TypedDict):
    observability_configuration_summary_list: "aws_sdk_apprunner.types.observability_configuration_summary_list.ObservabilityConfigurationSummaryList"
    """<p>A list of summary information records for observability configurations. In a paginated request, the request returns up to <code>MaxResults</code> records for each call.</p>"""
    next_token: NotRequired["aws_sdk_apprunner.types.next_token.NextToken"]
    """<p>The token that you can pass in a subsequent request to get the next result page. It's returned in a paginated request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListObservabilityConfigurationsResponse) -> dict:
    out: dict = {}
    import aws_sdk_apprunner.types.observability_configuration_summary_list

    out["ObservabilityConfigurationSummaryList"] = (
        aws_sdk_apprunner.types.observability_configuration_summary_list.serialize_aws_json_1_0(
            value["observability_configuration_summary_list"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListObservabilityConfigurationsResponse:
    out: ListObservabilityConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if "ObservabilityConfigurationSummaryList" in data:
        import aws_sdk_apprunner.types.observability_configuration_summary_list

        out["observability_configuration_summary_list"] = (
            aws_sdk_apprunner.types.observability_configuration_summary_list.deserialize_aws_json_1_0(
                data["ObservabilityConfigurationSummaryList"]
            )
        )
    else:
        raise DeserializationError(
            "ListObservabilityConfigurationsResponse.observability_configuration_summary_list required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
