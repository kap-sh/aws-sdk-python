"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListModelPackageGroupsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.creation_time
    import aws_sdk_sagemaker.types.cross_account_filter_option
    import aws_sdk_sagemaker.types.max_results
    import aws_sdk_sagemaker.types.model_package_group_sort_by
    import aws_sdk_sagemaker.types.name_contains
    import aws_sdk_sagemaker.types.next_token
    import aws_sdk_sagemaker.types.sort_order


class ListModelPackageGroupsInput(TypedDict):
    creation_time_after: NotRequired[
        "aws_sdk_sagemaker.types.creation_time.CreationTime"
    ]
    """<p>A filter that returns only model groups created after the specified time.</p>"""
    creation_time_before: NotRequired[
        "aws_sdk_sagemaker.types.creation_time.CreationTime"
    ]
    """<p>A filter that returns only model groups created before the specified time.</p>"""
    max_results: NotRequired["aws_sdk_sagemaker.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in the response.</p>"""
    name_contains: NotRequired["aws_sdk_sagemaker.types.name_contains.NameContains"]
    """<p>A string in the model group name. This filter returns only model groups whose name contains the specified string.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the result of the previous <code>ListModelPackageGroups</code> request was truncated, the response includes a <code>NextToken</code>. To retrieve the next set of model groups, use the token in the next request.</p>"""
    sort_by: NotRequired[
        "aws_sdk_sagemaker.types.model_package_group_sort_by.ModelPackageGroupSortBy"
    ]
    """<p>The field to sort results by. The default is <code>CreationTime</code>.</p>"""
    sort_order: NotRequired["aws_sdk_sagemaker.types.sort_order.SortOrder"]
    """<p>The sort order for results. The default is <code>Ascending</code>.</p>"""
    cross_account_filter_option: NotRequired[
        "aws_sdk_sagemaker.types.cross_account_filter_option.CrossAccountFilterOption"
    ]
    """<p>A filter that returns either model groups shared with you or model groups in your own account. When the value is <code>CrossAccount</code>, the results show the resources made discoverable to you from other accounts. When the value is <code>SameAccount</code> or <code>null</code>, the results show resources from your account. The default is <code>SameAccount</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListModelPackageGroupsInput) -> dict:
    out: dict = {}
    if "creation_time_after" in value:
        import aws_sdk_sagemaker.types.creation_time

        out["CreationTimeAfter"] = (
            aws_sdk_sagemaker.types.creation_time.serialize_aws_json_1_1(
                value["creation_time_after"]
            )
        )
    if "creation_time_before" in value:
        import aws_sdk_sagemaker.types.creation_time

        out["CreationTimeBefore"] = (
            aws_sdk_sagemaker.types.creation_time.serialize_aws_json_1_1(
                value["creation_time_before"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "name_contains" in value:
        out["NameContains"] = value["name_contains"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "sort_by" in value:
        import aws_sdk_sagemaker.types.model_package_group_sort_by

        out["SortBy"] = (
            aws_sdk_sagemaker.types.model_package_group_sort_by.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import aws_sdk_sagemaker.types.sort_order

        out["SortOrder"] = aws_sdk_sagemaker.types.sort_order.serialize_aws_json_1_1(
            value["sort_order"]
        )
    if "cross_account_filter_option" in value:
        import aws_sdk_sagemaker.types.cross_account_filter_option

        out["CrossAccountFilterOption"] = (
            aws_sdk_sagemaker.types.cross_account_filter_option.serialize_aws_json_1_1(
                value["cross_account_filter_option"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListModelPackageGroupsInput:
    out: ListModelPackageGroupsInput = {}  # type: ignore[typeddict-item]
    if "CreationTimeAfter" in data:
        import aws_sdk_sagemaker.types.creation_time

        out["creation_time_after"] = (
            aws_sdk_sagemaker.types.creation_time.deserialize_aws_json_1_1(
                data["CreationTimeAfter"]
            )
        )
    if "CreationTimeBefore" in data:
        import aws_sdk_sagemaker.types.creation_time

        out["creation_time_before"] = (
            aws_sdk_sagemaker.types.creation_time.deserialize_aws_json_1_1(
                data["CreationTimeBefore"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NameContains" in data:
        out["name_contains"] = data["NameContains"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "SortBy" in data:
        import aws_sdk_sagemaker.types.model_package_group_sort_by

        out["sort_by"] = (
            aws_sdk_sagemaker.types.model_package_group_sort_by.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    if "SortOrder" in data:
        import aws_sdk_sagemaker.types.sort_order

        out["sort_order"] = aws_sdk_sagemaker.types.sort_order.deserialize_aws_json_1_1(
            data["SortOrder"]
        )
    if "CrossAccountFilterOption" in data:
        import aws_sdk_sagemaker.types.cross_account_filter_option

        out["cross_account_filter_option"] = (
            aws_sdk_sagemaker.types.cross_account_filter_option.deserialize_aws_json_1_1(
                data["CrossAccountFilterOption"]
            )
        )
    return out
