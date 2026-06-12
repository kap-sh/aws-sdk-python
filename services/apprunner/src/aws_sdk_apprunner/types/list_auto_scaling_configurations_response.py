"""Generated from Smithy shape ``com.amazonaws.apprunner#ListAutoScalingConfigurationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_apprunner.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.auto_scaling_configuration_summary_list
    import aws_sdk_apprunner.types.next_token


class ListAutoScalingConfigurationsResponse(TypedDict):
    auto_scaling_configuration_summary_list: "aws_sdk_apprunner.types.auto_scaling_configuration_summary_list.AutoScalingConfigurationSummaryList"
    """<p>A list of summary information records for auto scaling configurations. In a paginated request, the request returns up to <code>MaxResults</code> records for each call.</p>"""
    next_token: NotRequired["aws_sdk_apprunner.types.next_token.NextToken"]
    """<p>The token that you can pass in a subsequent request to get the next result page. It's returned in a paginated request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAutoScalingConfigurationsResponse) -> dict:
    out: dict = {}
    import aws_sdk_apprunner.types.auto_scaling_configuration_summary_list

    out["AutoScalingConfigurationSummaryList"] = (
        aws_sdk_apprunner.types.auto_scaling_configuration_summary_list.serialize_aws_json_1_0(
            value["auto_scaling_configuration_summary_list"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAutoScalingConfigurationsResponse:
    out: ListAutoScalingConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if "AutoScalingConfigurationSummaryList" in data:
        import aws_sdk_apprunner.types.auto_scaling_configuration_summary_list

        out["auto_scaling_configuration_summary_list"] = (
            aws_sdk_apprunner.types.auto_scaling_configuration_summary_list.deserialize_aws_json_1_0(
                data["AutoScalingConfigurationSummaryList"]
            )
        )
    else:
        raise DeserializationError(
            "ListAutoScalingConfigurationsResponse.auto_scaling_configuration_summary_list required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
