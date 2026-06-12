"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListFeatureGroupsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.creation_time
    import aws_sdk_sagemaker.types.feature_group_max_results
    import aws_sdk_sagemaker.types.feature_group_name_contains
    import aws_sdk_sagemaker.types.feature_group_sort_by
    import aws_sdk_sagemaker.types.feature_group_sort_order
    import aws_sdk_sagemaker.types.feature_group_status
    import aws_sdk_sagemaker.types.next_token
    import aws_sdk_sagemaker.types.offline_store_status_value


class ListFeatureGroupsRequest(TypedDict):
    name_contains: NotRequired[
        "aws_sdk_sagemaker.types.feature_group_name_contains.FeatureGroupNameContains"
    ]
    """<p>A string that partially matches one or more <code>FeatureGroup</code>s names. Filters <code>FeatureGroup</code>s by name. </p>"""
    feature_group_status_equals: NotRequired[
        "aws_sdk_sagemaker.types.feature_group_status.FeatureGroupStatus"
    ]
    """<p>A <code>FeatureGroup</code> status. Filters by <code>FeatureGroup</code> status. </p>"""
    offline_store_status_equals: NotRequired[
        "aws_sdk_sagemaker.types.offline_store_status_value.OfflineStoreStatusValue"
    ]
    """<p>An <code>OfflineStore</code> status. Filters by <code>OfflineStore</code> status. </p>"""
    creation_time_after: NotRequired[
        "aws_sdk_sagemaker.types.creation_time.CreationTime"
    ]
    """<p>Use this parameter to search for <code>FeatureGroups</code>s created after a specific date and time.</p>"""
    creation_time_before: NotRequired[
        "aws_sdk_sagemaker.types.creation_time.CreationTime"
    ]
    """<p>Use this parameter to search for <code>FeatureGroups</code>s created before a specific date and time.</p>"""
    sort_order: NotRequired[
        "aws_sdk_sagemaker.types.feature_group_sort_order.FeatureGroupSortOrder"
    ]
    """<p>The order in which feature groups are listed.</p>"""
    sort_by: NotRequired[
        "aws_sdk_sagemaker.types.feature_group_sort_by.FeatureGroupSortBy"
    ]
    """<p>The value on which the feature group list is sorted.</p>"""
    max_results: NotRequired[
        "aws_sdk_sagemaker.types.feature_group_max_results.FeatureGroupMaxResults"
    ]
    """<p>The maximum number of results returned by <code>ListFeatureGroups</code>.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>A token to resume pagination of <code>ListFeatureGroups</code> results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListFeatureGroupsRequest) -> dict:
    out: dict = {}
    if "name_contains" in value:
        out["NameContains"] = value["name_contains"]
    if "feature_group_status_equals" in value:
        import aws_sdk_sagemaker.types.feature_group_status

        out["FeatureGroupStatusEquals"] = (
            aws_sdk_sagemaker.types.feature_group_status.serialize_aws_json_1_1(
                value["feature_group_status_equals"]
            )
        )
    if "offline_store_status_equals" in value:
        import aws_sdk_sagemaker.types.offline_store_status_value

        out["OfflineStoreStatusEquals"] = (
            aws_sdk_sagemaker.types.offline_store_status_value.serialize_aws_json_1_1(
                value["offline_store_status_equals"]
            )
        )
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
    if "sort_order" in value:
        import aws_sdk_sagemaker.types.feature_group_sort_order

        out["SortOrder"] = (
            aws_sdk_sagemaker.types.feature_group_sort_order.serialize_aws_json_1_1(
                value["sort_order"]
            )
        )
    if "sort_by" in value:
        import aws_sdk_sagemaker.types.feature_group_sort_by

        out["SortBy"] = (
            aws_sdk_sagemaker.types.feature_group_sort_by.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListFeatureGroupsRequest:
    out: ListFeatureGroupsRequest = {}  # type: ignore[typeddict-item]
    if "NameContains" in data:
        out["name_contains"] = data["NameContains"]
    if "FeatureGroupStatusEquals" in data:
        import aws_sdk_sagemaker.types.feature_group_status

        out["feature_group_status_equals"] = (
            aws_sdk_sagemaker.types.feature_group_status.deserialize_aws_json_1_1(
                data["FeatureGroupStatusEquals"]
            )
        )
    if "OfflineStoreStatusEquals" in data:
        import aws_sdk_sagemaker.types.offline_store_status_value

        out["offline_store_status_equals"] = (
            aws_sdk_sagemaker.types.offline_store_status_value.deserialize_aws_json_1_1(
                data["OfflineStoreStatusEquals"]
            )
        )
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
    if "SortOrder" in data:
        import aws_sdk_sagemaker.types.feature_group_sort_order

        out["sort_order"] = (
            aws_sdk_sagemaker.types.feature_group_sort_order.deserialize_aws_json_1_1(
                data["SortOrder"]
            )
        )
    if "SortBy" in data:
        import aws_sdk_sagemaker.types.feature_group_sort_by

        out["sort_by"] = (
            aws_sdk_sagemaker.types.feature_group_sort_by.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
