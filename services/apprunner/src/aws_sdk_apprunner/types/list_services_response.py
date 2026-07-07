"""Generated from Smithy shape ``com.amazonaws.apprunner#ListServicesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_apprunner.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.service_summary_list
    import aws_sdk_apprunner.types.string


class ListServicesResponse(TypedDict, closed=True):
    service_summary_list: (
        "aws_sdk_apprunner.types.service_summary_list.ServiceSummaryList"
    )
    """<p>A list of service summary information records. In a paginated request, the request returns up to <code>MaxResults</code> records for each call.</p>"""
    next_token: NotRequired["aws_sdk_apprunner.types.string.String"]
    """<p>The token that you can pass in a subsequent request to get the next result page. It's returned in a paginated request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListServicesResponse) -> dict:
    out: dict = {}
    import aws_sdk_apprunner.types.service_summary_list

    out["ServiceSummaryList"] = (
        aws_sdk_apprunner.types.service_summary_list.serialize_aws_json_1_0(
            value["service_summary_list"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListServicesResponse:
    out: ListServicesResponse = {}  # type: ignore[typeddict-item]
    if "ServiceSummaryList" in data:
        import aws_sdk_apprunner.types.service_summary_list

        out["service_summary_list"] = (
            aws_sdk_apprunner.types.service_summary_list.deserialize_aws_json_1_0(
                data["ServiceSummaryList"]
            )
        )
    else:
        raise DeserializationError("ListServicesResponse.service_summary_list required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
