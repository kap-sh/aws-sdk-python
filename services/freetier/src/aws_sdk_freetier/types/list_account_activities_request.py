"""Generated from Smithy shape ``com.amazonaws.freetier#ListAccountActivitiesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_freetier.types.filter_activity_statuses
    import aws_sdk_freetier.types.language_code
    import aws_sdk_freetier.types.max_results
    import aws_sdk_freetier.types.next_page_token


class ListAccountActivitiesRequest(TypedDict, closed=True):
    filter_activity_statuses: NotRequired[
        "aws_sdk_freetier.types.filter_activity_statuses.FilterActivityStatuses"
    ]
    """<p> The activity status filter. This field can be used to filter the response by activities status. </p>"""
    next_token: NotRequired["aws_sdk_freetier.types.next_page_token.NextPageToken"]
    """<p> A token from a previous paginated response. If this is specified, the response includes records beginning from this token (inclusive), up to the number specified by <code>maxResults</code>. </p>"""
    max_results: "aws_sdk_freetier.types.max_results.MaxResults"
    """<p> The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. </p>"""
    language_code: NotRequired["aws_sdk_freetier.types.language_code.LanguageCode"]
    """<p> The language code used to return translated titles. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAccountActivitiesRequest) -> dict:
    out: dict = {}
    if "filter_activity_statuses" in value:
        import aws_sdk_freetier.types.filter_activity_statuses

        out["filterActivityStatuses"] = (
            aws_sdk_freetier.types.filter_activity_statuses.serialize_aws_json_1_0(
                value["filter_activity_statuses"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    out["maxResults"] = value.get("max_results", 10)
    if "language_code" in value:
        import aws_sdk_freetier.types.language_code

        out["languageCode"] = (
            aws_sdk_freetier.types.language_code.serialize_aws_json_1_0(
                value["language_code"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAccountActivitiesRequest:
    out: ListAccountActivitiesRequest = {}  # type: ignore[typeddict-item]
    if "filterActivityStatuses" in data:
        import aws_sdk_freetier.types.filter_activity_statuses

        out["filter_activity_statuses"] = (
            aws_sdk_freetier.types.filter_activity_statuses.deserialize_aws_json_1_0(
                data["filterActivityStatuses"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    else:
        out["max_results"] = 10
    if "languageCode" in data:
        import aws_sdk_freetier.types.language_code

        out["language_code"] = (
            aws_sdk_freetier.types.language_code.deserialize_aws_json_1_0(
                data["languageCode"]
            )
        )
    return out
