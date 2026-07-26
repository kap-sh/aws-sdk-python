"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListNotebookInstanceLifecycleConfigsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.creation_time
    import capo_sagemaker.types.last_modified_time
    import capo_sagemaker.types.max_results
    import capo_sagemaker.types.next_token
    import capo_sagemaker.types.notebook_instance_lifecycle_config_name_contains
    import capo_sagemaker.types.notebook_instance_lifecycle_config_sort_key
    import capo_sagemaker.types.notebook_instance_lifecycle_config_sort_order


class ListNotebookInstanceLifecycleConfigsInput(TypedDict, closed=True):
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>If the result of a <code>ListNotebookInstanceLifecycleConfigs</code> request was truncated, the response includes a <code>NextToken</code>. To get the next set of lifecycle configurations, use the token in the next request.</p>"""
    max_results: NotRequired["capo_sagemaker.types.max_results.MaxResults"]
    """<p>The maximum number of lifecycle configurations to return in the response.</p>"""
    sort_by: NotRequired[
        "capo_sagemaker.types.notebook_instance_lifecycle_config_sort_key.NotebookInstanceLifecycleConfigSortKey"
    ]
    """<p>Sorts the list of results. The default is <code>CreationTime</code>.</p>"""
    sort_order: NotRequired[
        "capo_sagemaker.types.notebook_instance_lifecycle_config_sort_order.NotebookInstanceLifecycleConfigSortOrder"
    ]
    """<p>The sort order for results.</p>"""
    name_contains: NotRequired[
        "capo_sagemaker.types.notebook_instance_lifecycle_config_name_contains.NotebookInstanceLifecycleConfigNameContains"
    ]
    """<p>A string in the lifecycle configuration name. This filter returns only lifecycle configurations whose name contains the specified string.</p>"""
    creation_time_before: NotRequired["capo_sagemaker.types.creation_time.CreationTime"]
    """<p>A filter that returns only lifecycle configurations that were created before the specified time (timestamp).</p>"""
    creation_time_after: NotRequired["capo_sagemaker.types.creation_time.CreationTime"]
    """<p>A filter that returns only lifecycle configurations that were created after the specified time (timestamp).</p>"""
    last_modified_time_before: NotRequired[
        "capo_sagemaker.types.last_modified_time.LastModifiedTime"
    ]
    """<p>A filter that returns only lifecycle configurations that were modified before the specified time (timestamp).</p>"""
    last_modified_time_after: NotRequired[
        "capo_sagemaker.types.last_modified_time.LastModifiedTime"
    ]
    """<p>A filter that returns only lifecycle configurations that were modified after the specified time (timestamp).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListNotebookInstanceLifecycleConfigsInput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "sort_by" in value:
        import capo_sagemaker.types.notebook_instance_lifecycle_config_sort_key

        out["SortBy"] = (
            capo_sagemaker.types.notebook_instance_lifecycle_config_sort_key.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import capo_sagemaker.types.notebook_instance_lifecycle_config_sort_order

        out["SortOrder"] = (
            capo_sagemaker.types.notebook_instance_lifecycle_config_sort_order.serialize_aws_json_1_1(
                value["sort_order"]
            )
        )
    if "name_contains" in value:
        out["NameContains"] = value["name_contains"]
    if "creation_time_before" in value:
        import capo_sagemaker.types.creation_time

        out["CreationTimeBefore"] = (
            capo_sagemaker.types.creation_time.serialize_aws_json_1_1(
                value["creation_time_before"]
            )
        )
    if "creation_time_after" in value:
        import capo_sagemaker.types.creation_time

        out["CreationTimeAfter"] = (
            capo_sagemaker.types.creation_time.serialize_aws_json_1_1(
                value["creation_time_after"]
            )
        )
    if "last_modified_time_before" in value:
        import capo_sagemaker.types.last_modified_time

        out["LastModifiedTimeBefore"] = (
            capo_sagemaker.types.last_modified_time.serialize_aws_json_1_1(
                value["last_modified_time_before"]
            )
        )
    if "last_modified_time_after" in value:
        import capo_sagemaker.types.last_modified_time

        out["LastModifiedTimeAfter"] = (
            capo_sagemaker.types.last_modified_time.serialize_aws_json_1_1(
                value["last_modified_time_after"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListNotebookInstanceLifecycleConfigsInput:
    out: ListNotebookInstanceLifecycleConfigsInput = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "SortBy" in data:
        import capo_sagemaker.types.notebook_instance_lifecycle_config_sort_key

        out["sort_by"] = (
            capo_sagemaker.types.notebook_instance_lifecycle_config_sort_key.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    if "SortOrder" in data:
        import capo_sagemaker.types.notebook_instance_lifecycle_config_sort_order

        out["sort_order"] = (
            capo_sagemaker.types.notebook_instance_lifecycle_config_sort_order.deserialize_aws_json_1_1(
                data["SortOrder"]
            )
        )
    if "NameContains" in data:
        out["name_contains"] = data["NameContains"]
    if "CreationTimeBefore" in data:
        import capo_sagemaker.types.creation_time

        out["creation_time_before"] = (
            capo_sagemaker.types.creation_time.deserialize_aws_json_1_1(
                data["CreationTimeBefore"]
            )
        )
    if "CreationTimeAfter" in data:
        import capo_sagemaker.types.creation_time

        out["creation_time_after"] = (
            capo_sagemaker.types.creation_time.deserialize_aws_json_1_1(
                data["CreationTimeAfter"]
            )
        )
    if "LastModifiedTimeBefore" in data:
        import capo_sagemaker.types.last_modified_time

        out["last_modified_time_before"] = (
            capo_sagemaker.types.last_modified_time.deserialize_aws_json_1_1(
                data["LastModifiedTimeBefore"]
            )
        )
    if "LastModifiedTimeAfter" in data:
        import capo_sagemaker.types.last_modified_time

        out["last_modified_time_after"] = (
            capo_sagemaker.types.last_modified_time.deserialize_aws_json_1_1(
                data["LastModifiedTimeAfter"]
            )
        )
    return out
