"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListCodeRepositoriesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.code_repository_name_contains
    import aws_sdk_sagemaker.types.code_repository_sort_by
    import aws_sdk_sagemaker.types.code_repository_sort_order
    import aws_sdk_sagemaker.types.creation_time
    import aws_sdk_sagemaker.types.max_results
    import aws_sdk_sagemaker.types.next_token
    import aws_sdk_sagemaker.types.timestamp


class ListCodeRepositoriesInput(TypedDict, closed=True):
    creation_time_after: NotRequired[
        "aws_sdk_sagemaker.types.creation_time.CreationTime"
    ]
    """<p>A filter that returns only Git repositories that were created after the specified time.</p>"""
    creation_time_before: NotRequired[
        "aws_sdk_sagemaker.types.creation_time.CreationTime"
    ]
    """<p>A filter that returns only Git repositories that were created before the specified time.</p>"""
    last_modified_time_after: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>A filter that returns only Git repositories that were last modified after the specified time.</p>"""
    last_modified_time_before: NotRequired[
        "aws_sdk_sagemaker.types.timestamp.Timestamp"
    ]
    """<p>A filter that returns only Git repositories that were last modified before the specified time.</p>"""
    max_results: NotRequired["aws_sdk_sagemaker.types.max_results.MaxResults"]
    """<p>The maximum number of Git repositories to return in the response.</p>"""
    name_contains: NotRequired[
        "aws_sdk_sagemaker.types.code_repository_name_contains.CodeRepositoryNameContains"
    ]
    """<p>A string in the Git repositories name. This filter returns only repositories whose name contains the specified string.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the result of a <code>ListCodeRepositoriesOutput</code> request was truncated, the response includes a <code>NextToken</code>. To get the next set of Git repositories, use the token in the next request.</p>"""
    sort_by: NotRequired[
        "aws_sdk_sagemaker.types.code_repository_sort_by.CodeRepositorySortBy"
    ]
    """<p>The field to sort results by. The default is <code>Name</code>.</p>"""
    sort_order: NotRequired[
        "aws_sdk_sagemaker.types.code_repository_sort_order.CodeRepositorySortOrder"
    ]
    """<p>The sort order for results. The default is <code>Ascending</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCodeRepositoriesInput) -> dict:
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
    if "last_modified_time_after" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["LastModifiedTimeAfter"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time_after"]
            )
        )
    if "last_modified_time_before" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["LastModifiedTimeBefore"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time_before"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "name_contains" in value:
        out["NameContains"] = value["name_contains"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "sort_by" in value:
        import aws_sdk_sagemaker.types.code_repository_sort_by

        out["SortBy"] = (
            aws_sdk_sagemaker.types.code_repository_sort_by.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import aws_sdk_sagemaker.types.code_repository_sort_order

        out["SortOrder"] = (
            aws_sdk_sagemaker.types.code_repository_sort_order.serialize_aws_json_1_1(
                value["sort_order"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCodeRepositoriesInput:
    out: ListCodeRepositoriesInput = {}  # type: ignore[typeddict-item]
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
    if "LastModifiedTimeAfter" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["last_modified_time_after"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTimeAfter"]
            )
        )
    if "LastModifiedTimeBefore" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["last_modified_time_before"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTimeBefore"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NameContains" in data:
        out["name_contains"] = data["NameContains"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "SortBy" in data:
        import aws_sdk_sagemaker.types.code_repository_sort_by

        out["sort_by"] = (
            aws_sdk_sagemaker.types.code_repository_sort_by.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    if "SortOrder" in data:
        import aws_sdk_sagemaker.types.code_repository_sort_order

        out["sort_order"] = (
            aws_sdk_sagemaker.types.code_repository_sort_order.deserialize_aws_json_1_1(
                data["SortOrder"]
            )
        )
    return out
