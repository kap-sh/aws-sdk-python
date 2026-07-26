"""Generated from Smithy shape ``com.amazonaws.applicationinsights#ListApplicationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_insights.types.application_info_list
    import capo_application_insights.types.pagination_token


class ListApplicationsResponse(TypedDict, closed=True):
    application_info_list: NotRequired[
        "capo_application_insights.types.application_info_list.ApplicationInfoList"
    ]
    """<p>The list of applications.</p>"""
    next_token: NotRequired[
        "capo_application_insights.types.pagination_token.PaginationToken"
    ]
    """<p>The token used to retrieve the next page of results. This value is <code>null</code> when there are no more results to return. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListApplicationsResponse) -> dict:
    out: dict = {}
    if "application_info_list" in value:
        import capo_application_insights.types.application_info_list

        out["ApplicationInfoList"] = (
            capo_application_insights.types.application_info_list.serialize_aws_json_1_1(
                value["application_info_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListApplicationsResponse:
    out: ListApplicationsResponse = {}  # type: ignore[typeddict-item]
    if "ApplicationInfoList" in data:
        import capo_application_insights.types.application_info_list

        out["application_info_list"] = (
            capo_application_insights.types.application_info_list.deserialize_aws_json_1_1(
                data["ApplicationInfoList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
