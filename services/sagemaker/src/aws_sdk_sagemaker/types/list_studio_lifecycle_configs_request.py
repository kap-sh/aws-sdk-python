"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListStudioLifecycleConfigsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.max_results
    import aws_sdk_sagemaker.types.next_token
    import aws_sdk_sagemaker.types.sort_order
    import aws_sdk_sagemaker.types.studio_lifecycle_config_app_type
    import aws_sdk_sagemaker.types.studio_lifecycle_config_name
    import aws_sdk_sagemaker.types.studio_lifecycle_config_sort_key
    import aws_sdk_sagemaker.types.timestamp


class ListStudioLifecycleConfigsRequest(TypedDict):
    max_results: NotRequired["aws_sdk_sagemaker.types.max_results.MaxResults"]
    """<p>The total number of items to return in the response. If the total number of items available is more than the value specified, a <code>NextToken</code> is provided in the response. To resume pagination, provide the <code>NextToken</code> value in the as part of a subsequent call. The default value is 10.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the previous call to ListStudioLifecycleConfigs didn't return the full set of Lifecycle Configurations, the call returns a token for getting the next set of Lifecycle Configurations.</p>"""
    name_contains: NotRequired[
        "aws_sdk_sagemaker.types.studio_lifecycle_config_name.StudioLifecycleConfigName"
    ]
    """<p>A string in the Lifecycle Configuration name. This filter returns only Lifecycle Configurations whose name contains the specified string.</p>"""
    app_type_equals: NotRequired[
        "aws_sdk_sagemaker.types.studio_lifecycle_config_app_type.StudioLifecycleConfigAppType"
    ]
    """<p>A parameter to search for the App Type to which the Lifecycle Configuration is attached.</p>"""
    creation_time_before: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>A filter that returns only Lifecycle Configurations created on or before the specified time.</p>"""
    creation_time_after: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>A filter that returns only Lifecycle Configurations created on or after the specified time.</p>"""
    modified_time_before: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>A filter that returns only Lifecycle Configurations modified before the specified time.</p>"""
    modified_time_after: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>A filter that returns only Lifecycle Configurations modified after the specified time.</p>"""
    sort_by: NotRequired[
        "aws_sdk_sagemaker.types.studio_lifecycle_config_sort_key.StudioLifecycleConfigSortKey"
    ]
    """<p>The property used to sort results. The default value is CreationTime.</p>"""
    sort_order: NotRequired["aws_sdk_sagemaker.types.sort_order.SortOrder"]
    """<p>The sort order. The default value is Descending.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListStudioLifecycleConfigsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "name_contains" in value:
        out["NameContains"] = value["name_contains"]
    if "app_type_equals" in value:
        import aws_sdk_sagemaker.types.studio_lifecycle_config_app_type

        out["AppTypeEquals"] = (
            aws_sdk_sagemaker.types.studio_lifecycle_config_app_type.serialize_aws_json_1_1(
                value["app_type_equals"]
            )
        )
    if "creation_time_before" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTimeBefore"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["creation_time_before"]
            )
        )
    if "creation_time_after" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTimeAfter"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["creation_time_after"]
            )
        )
    if "modified_time_before" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["ModifiedTimeBefore"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["modified_time_before"]
            )
        )
    if "modified_time_after" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["ModifiedTimeAfter"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["modified_time_after"]
            )
        )
    if "sort_by" in value:
        import aws_sdk_sagemaker.types.studio_lifecycle_config_sort_key

        out["SortBy"] = (
            aws_sdk_sagemaker.types.studio_lifecycle_config_sort_key.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import aws_sdk_sagemaker.types.sort_order

        out["SortOrder"] = aws_sdk_sagemaker.types.sort_order.serialize_aws_json_1_1(
            value["sort_order"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListStudioLifecycleConfigsRequest:
    out: ListStudioLifecycleConfigsRequest = {}  # type: ignore[typeddict-item]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "NameContains" in data:
        out["name_contains"] = data["NameContains"]
    if "AppTypeEquals" in data:
        import aws_sdk_sagemaker.types.studio_lifecycle_config_app_type

        out["app_type_equals"] = (
            aws_sdk_sagemaker.types.studio_lifecycle_config_app_type.deserialize_aws_json_1_1(
                data["AppTypeEquals"]
            )
        )
    if "CreationTimeBefore" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time_before"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTimeBefore"]
            )
        )
    if "CreationTimeAfter" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time_after"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTimeAfter"]
            )
        )
    if "ModifiedTimeBefore" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["modified_time_before"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["ModifiedTimeBefore"]
            )
        )
    if "ModifiedTimeAfter" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["modified_time_after"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["ModifiedTimeAfter"]
            )
        )
    if "SortBy" in data:
        import aws_sdk_sagemaker.types.studio_lifecycle_config_sort_key

        out["sort_by"] = (
            aws_sdk_sagemaker.types.studio_lifecycle_config_sort_key.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    if "SortOrder" in data:
        import aws_sdk_sagemaker.types.sort_order

        out["sort_order"] = aws_sdk_sagemaker.types.sort_order.deserialize_aws_json_1_1(
            data["SortOrder"]
        )
    return out
