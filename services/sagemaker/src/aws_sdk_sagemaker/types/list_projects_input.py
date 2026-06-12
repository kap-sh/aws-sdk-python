"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListProjectsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.max_results
    import aws_sdk_sagemaker.types.next_token
    import aws_sdk_sagemaker.types.project_entity_name
    import aws_sdk_sagemaker.types.project_sort_by
    import aws_sdk_sagemaker.types.project_sort_order
    import aws_sdk_sagemaker.types.timestamp


class ListProjectsInput(TypedDict):
    creation_time_after: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>A filter that returns the projects that were created after a specified time.</p>"""
    creation_time_before: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>A filter that returns the projects that were created before a specified time.</p>"""
    max_results: NotRequired["aws_sdk_sagemaker.types.max_results.MaxResults"]
    """<p>The maximum number of projects to return in the response.</p>"""
    name_contains: NotRequired[
        "aws_sdk_sagemaker.types.project_entity_name.ProjectEntityName"
    ]
    """<p>A filter that returns the projects whose name contains a specified string.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the result of the previous <code>ListProjects</code> request was truncated, the response includes a <code>NextToken</code>. To retrieve the next set of projects, use the token in the next request.</p>"""
    sort_by: NotRequired["aws_sdk_sagemaker.types.project_sort_by.ProjectSortBy"]
    """<p>The field by which to sort results. The default is <code>CreationTime</code>.</p>"""
    sort_order: NotRequired[
        "aws_sdk_sagemaker.types.project_sort_order.ProjectSortOrder"
    ]
    """<p>The sort order for results. The default is <code>Ascending</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListProjectsInput) -> dict:
    out: dict = {}
    if "creation_time_after" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTimeAfter"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["creation_time_after"]
            )
        )
    if "creation_time_before" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTimeBefore"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
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
        import aws_sdk_sagemaker.types.project_sort_by

        out["SortBy"] = aws_sdk_sagemaker.types.project_sort_by.serialize_aws_json_1_1(
            value["sort_by"]
        )
    if "sort_order" in value:
        import aws_sdk_sagemaker.types.project_sort_order

        out["SortOrder"] = (
            aws_sdk_sagemaker.types.project_sort_order.serialize_aws_json_1_1(
                value["sort_order"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListProjectsInput:
    out: ListProjectsInput = {}  # type: ignore[typeddict-item]
    if "CreationTimeAfter" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time_after"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTimeAfter"]
            )
        )
    if "CreationTimeBefore" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time_before"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
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
        import aws_sdk_sagemaker.types.project_sort_by

        out["sort_by"] = (
            aws_sdk_sagemaker.types.project_sort_by.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    if "SortOrder" in data:
        import aws_sdk_sagemaker.types.project_sort_order

        out["sort_order"] = (
            aws_sdk_sagemaker.types.project_sort_order.deserialize_aws_json_1_1(
                data["SortOrder"]
            )
        )
    return out
