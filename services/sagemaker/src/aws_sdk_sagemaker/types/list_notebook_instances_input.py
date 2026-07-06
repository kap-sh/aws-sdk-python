"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListNotebookInstancesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.code_repository_contains
    import aws_sdk_sagemaker.types.code_repository_name_or_url
    import aws_sdk_sagemaker.types.creation_time
    import aws_sdk_sagemaker.types.last_modified_time
    import aws_sdk_sagemaker.types.max_results
    import aws_sdk_sagemaker.types.next_token
    import aws_sdk_sagemaker.types.notebook_instance_lifecycle_config_name
    import aws_sdk_sagemaker.types.notebook_instance_name_contains
    import aws_sdk_sagemaker.types.notebook_instance_sort_key
    import aws_sdk_sagemaker.types.notebook_instance_sort_order
    import aws_sdk_sagemaker.types.notebook_instance_status


class ListNotebookInstancesInput(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p> If the previous call to the <code>ListNotebookInstances</code> is truncated, the response includes a <code>NextToken</code>. You can use this token in your subsequent <code>ListNotebookInstances</code> request to fetch the next set of notebook instances. </p> <note> <p>You might specify a filter or a sort order in your request. When response is truncated, you must use the same values for the filer and sort order in the next request. </p> </note>"""
    max_results: NotRequired["aws_sdk_sagemaker.types.max_results.MaxResults"]
    """<p>The maximum number of notebook instances to return.</p>"""
    sort_by: NotRequired[
        "aws_sdk_sagemaker.types.notebook_instance_sort_key.NotebookInstanceSortKey"
    ]
    """<p>The field to sort results by. The default is <code>Name</code>.</p>"""
    sort_order: NotRequired[
        "aws_sdk_sagemaker.types.notebook_instance_sort_order.NotebookInstanceSortOrder"
    ]
    """<p>The sort order for results. </p>"""
    name_contains: NotRequired[
        "aws_sdk_sagemaker.types.notebook_instance_name_contains.NotebookInstanceNameContains"
    ]
    """<p>A string in the notebook instances' name. This filter returns only notebook instances whose name contains the specified string.</p>"""
    creation_time_before: NotRequired[
        "aws_sdk_sagemaker.types.creation_time.CreationTime"
    ]
    """<p>A filter that returns only notebook instances that were created before the specified time (timestamp). </p>"""
    creation_time_after: NotRequired[
        "aws_sdk_sagemaker.types.creation_time.CreationTime"
    ]
    """<p>A filter that returns only notebook instances that were created after the specified time (timestamp).</p>"""
    last_modified_time_before: NotRequired[
        "aws_sdk_sagemaker.types.last_modified_time.LastModifiedTime"
    ]
    """<p>A filter that returns only notebook instances that were modified before the specified time (timestamp).</p>"""
    last_modified_time_after: NotRequired[
        "aws_sdk_sagemaker.types.last_modified_time.LastModifiedTime"
    ]
    """<p>A filter that returns only notebook instances that were modified after the specified time (timestamp).</p>"""
    status_equals: NotRequired[
        "aws_sdk_sagemaker.types.notebook_instance_status.NotebookInstanceStatus"
    ]
    """<p>A filter that returns only notebook instances with the specified status.</p>"""
    notebook_instance_lifecycle_config_name_contains: NotRequired[
        "aws_sdk_sagemaker.types.notebook_instance_lifecycle_config_name.NotebookInstanceLifecycleConfigName"
    ]
    """<p>A string in the name of a notebook instances lifecycle configuration associated with this notebook instance. This filter returns only notebook instances associated with a lifecycle configuration with a name that contains the specified string.</p>"""
    default_code_repository_contains: NotRequired[
        "aws_sdk_sagemaker.types.code_repository_contains.CodeRepositoryContains"
    ]
    """<p>A string in the name or URL of a Git repository associated with this notebook instance. This filter returns only notebook instances associated with a git repository with a name that contains the specified string.</p>"""
    additional_code_repository_equals: NotRequired[
        "aws_sdk_sagemaker.types.code_repository_name_or_url.CodeRepositoryNameOrUrl"
    ]
    """<p>A filter that returns only notebook instances with associated with the specified git repository.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListNotebookInstancesInput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "sort_by" in value:
        import aws_sdk_sagemaker.types.notebook_instance_sort_key

        out["SortBy"] = (
            aws_sdk_sagemaker.types.notebook_instance_sort_key.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import aws_sdk_sagemaker.types.notebook_instance_sort_order

        out["SortOrder"] = (
            aws_sdk_sagemaker.types.notebook_instance_sort_order.serialize_aws_json_1_1(
                value["sort_order"]
            )
        )
    if "name_contains" in value:
        out["NameContains"] = value["name_contains"]
    if "creation_time_before" in value:
        import aws_sdk_sagemaker.types.creation_time

        out["CreationTimeBefore"] = (
            aws_sdk_sagemaker.types.creation_time.serialize_aws_json_1_1(
                value["creation_time_before"]
            )
        )
    if "creation_time_after" in value:
        import aws_sdk_sagemaker.types.creation_time

        out["CreationTimeAfter"] = (
            aws_sdk_sagemaker.types.creation_time.serialize_aws_json_1_1(
                value["creation_time_after"]
            )
        )
    if "last_modified_time_before" in value:
        import aws_sdk_sagemaker.types.last_modified_time

        out["LastModifiedTimeBefore"] = (
            aws_sdk_sagemaker.types.last_modified_time.serialize_aws_json_1_1(
                value["last_modified_time_before"]
            )
        )
    if "last_modified_time_after" in value:
        import aws_sdk_sagemaker.types.last_modified_time

        out["LastModifiedTimeAfter"] = (
            aws_sdk_sagemaker.types.last_modified_time.serialize_aws_json_1_1(
                value["last_modified_time_after"]
            )
        )
    if "status_equals" in value:
        import aws_sdk_sagemaker.types.notebook_instance_status

        out["StatusEquals"] = (
            aws_sdk_sagemaker.types.notebook_instance_status.serialize_aws_json_1_1(
                value["status_equals"]
            )
        )
    if "notebook_instance_lifecycle_config_name_contains" in value:
        out["NotebookInstanceLifecycleConfigNameContains"] = value[
            "notebook_instance_lifecycle_config_name_contains"
        ]
    if "default_code_repository_contains" in value:
        out["DefaultCodeRepositoryContains"] = value["default_code_repository_contains"]
    if "additional_code_repository_equals" in value:
        out["AdditionalCodeRepositoryEquals"] = value[
            "additional_code_repository_equals"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListNotebookInstancesInput:
    out: ListNotebookInstancesInput = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "SortBy" in data:
        import aws_sdk_sagemaker.types.notebook_instance_sort_key

        out["sort_by"] = (
            aws_sdk_sagemaker.types.notebook_instance_sort_key.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    if "SortOrder" in data:
        import aws_sdk_sagemaker.types.notebook_instance_sort_order

        out["sort_order"] = (
            aws_sdk_sagemaker.types.notebook_instance_sort_order.deserialize_aws_json_1_1(
                data["SortOrder"]
            )
        )
    if "NameContains" in data:
        out["name_contains"] = data["NameContains"]
    if "CreationTimeBefore" in data:
        import aws_sdk_sagemaker.types.creation_time

        out["creation_time_before"] = (
            aws_sdk_sagemaker.types.creation_time.deserialize_aws_json_1_1(
                data["CreationTimeBefore"]
            )
        )
    if "CreationTimeAfter" in data:
        import aws_sdk_sagemaker.types.creation_time

        out["creation_time_after"] = (
            aws_sdk_sagemaker.types.creation_time.deserialize_aws_json_1_1(
                data["CreationTimeAfter"]
            )
        )
    if "LastModifiedTimeBefore" in data:
        import aws_sdk_sagemaker.types.last_modified_time

        out["last_modified_time_before"] = (
            aws_sdk_sagemaker.types.last_modified_time.deserialize_aws_json_1_1(
                data["LastModifiedTimeBefore"]
            )
        )
    if "LastModifiedTimeAfter" in data:
        import aws_sdk_sagemaker.types.last_modified_time

        out["last_modified_time_after"] = (
            aws_sdk_sagemaker.types.last_modified_time.deserialize_aws_json_1_1(
                data["LastModifiedTimeAfter"]
            )
        )
    if "StatusEquals" in data:
        import aws_sdk_sagemaker.types.notebook_instance_status

        out["status_equals"] = (
            aws_sdk_sagemaker.types.notebook_instance_status.deserialize_aws_json_1_1(
                data["StatusEquals"]
            )
        )
    if "NotebookInstanceLifecycleConfigNameContains" in data:
        out["notebook_instance_lifecycle_config_name_contains"] = data[
            "NotebookInstanceLifecycleConfigNameContains"
        ]
    if "DefaultCodeRepositoryContains" in data:
        out["default_code_repository_contains"] = data["DefaultCodeRepositoryContains"]
    if "AdditionalCodeRepositoryEquals" in data:
        out["additional_code_repository_equals"] = data[
            "AdditionalCodeRepositoryEquals"
        ]
    return out
