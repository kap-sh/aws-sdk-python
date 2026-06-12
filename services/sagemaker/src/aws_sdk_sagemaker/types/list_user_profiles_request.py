"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListUserProfilesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.domain_id
    import aws_sdk_sagemaker.types.max_results
    import aws_sdk_sagemaker.types.next_token
    import aws_sdk_sagemaker.types.sort_order
    import aws_sdk_sagemaker.types.user_profile_name
    import aws_sdk_sagemaker.types.user_profile_sort_key


class ListUserProfilesRequest(TypedDict):
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the previous response was truncated, you will receive this token. Use it in your next request to receive the next set of results.</p>"""
    max_results: NotRequired["aws_sdk_sagemaker.types.max_results.MaxResults"]
    """<p>This parameter defines the maximum number of results that can be return in a single response. The <code>MaxResults</code> parameter is an upper bound, not a target. If there are more results available than the value specified, a <code>NextToken</code> is provided in the response. The <code>NextToken</code> indicates that the user should get the next set of results by providing this token as a part of a subsequent call. The default value for <code>MaxResults</code> is 10.</p>"""
    sort_order: NotRequired["aws_sdk_sagemaker.types.sort_order.SortOrder"]
    """<p>The sort order for the results. The default is Ascending.</p>"""
    sort_by: NotRequired[
        "aws_sdk_sagemaker.types.user_profile_sort_key.UserProfileSortKey"
    ]
    """<p>The parameter by which to sort the results. The default is CreationTime.</p>"""
    domain_id_equals: NotRequired["aws_sdk_sagemaker.types.domain_id.DomainId"]
    """<p>A parameter by which to filter the results.</p>"""
    user_profile_name_contains: NotRequired[
        "aws_sdk_sagemaker.types.user_profile_name.UserProfileName"
    ]
    """<p>A parameter by which to filter the results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListUserProfilesRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "sort_order" in value:
        import aws_sdk_sagemaker.types.sort_order

        out["SortOrder"] = aws_sdk_sagemaker.types.sort_order.serialize_aws_json_1_1(
            value["sort_order"]
        )
    if "sort_by" in value:
        import aws_sdk_sagemaker.types.user_profile_sort_key

        out["SortBy"] = (
            aws_sdk_sagemaker.types.user_profile_sort_key.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "domain_id_equals" in value:
        out["DomainIdEquals"] = value["domain_id_equals"]
    if "user_profile_name_contains" in value:
        out["UserProfileNameContains"] = value["user_profile_name_contains"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListUserProfilesRequest:
    out: ListUserProfilesRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "SortOrder" in data:
        import aws_sdk_sagemaker.types.sort_order

        out["sort_order"] = aws_sdk_sagemaker.types.sort_order.deserialize_aws_json_1_1(
            data["SortOrder"]
        )
    if "SortBy" in data:
        import aws_sdk_sagemaker.types.user_profile_sort_key

        out["sort_by"] = (
            aws_sdk_sagemaker.types.user_profile_sort_key.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    if "DomainIdEquals" in data:
        out["domain_id_equals"] = data["DomainIdEquals"]
    if "UserProfileNameContains" in data:
        out["user_profile_name_contains"] = data["UserProfileNameContains"]
    return out
