"""Generated from Smithy shape ``com.amazonaws.apprunner#ListServicesForAutoScalingConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_apprunner.errors import DeserializationError

if TYPE_CHECKING:
    import capo_apprunner.types.next_token
    import capo_apprunner.types.service_arn_list


class ListServicesForAutoScalingConfigurationResponse(TypedDict, closed=True):
    service_arn_list: "capo_apprunner.types.service_arn_list.ServiceArnList"
    """<p>A list of service ARN records. In a paginated request, the request returns up to <code>MaxResults</code> records for each call.</p>"""
    next_token: NotRequired["capo_apprunner.types.next_token.NextToken"]
    """<p>The token that you can pass in a subsequent request to get the next result page. It's returned in a paginated request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: ListServicesForAutoScalingConfigurationResponse,
) -> dict:
    out: dict = {}
    import capo_apprunner.types.service_arn_list

    out["ServiceArnList"] = (
        capo_apprunner.types.service_arn_list.serialize_aws_json_1_0(
            value["service_arn_list"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> ListServicesForAutoScalingConfigurationResponse:
    out: ListServicesForAutoScalingConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "ServiceArnList" in data:
        import capo_apprunner.types.service_arn_list

        out["service_arn_list"] = (
            capo_apprunner.types.service_arn_list.deserialize_aws_json_1_0(
                data["ServiceArnList"]
            )
        )
    else:
        raise DeserializationError(
            "ListServicesForAutoScalingConfigurationResponse.service_arn_list required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
