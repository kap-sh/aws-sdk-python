"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListProjectsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.next_token
    import capo_sagemaker.types.project_summary_list


class ListProjectsOutput(TypedDict, closed=True):
    project_summary_list: NotRequired[
        "capo_sagemaker.types.project_summary_list.ProjectSummaryList"
    ]
    """<p>A list of summaries of projects.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>If the result of the previous <code>ListCompilationJobs</code> request was truncated, the response includes a <code>NextToken</code>. To retrieve the next set of model compilation jobs, use the token in the next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListProjectsOutput) -> dict:
    out: dict = {}
    if "project_summary_list" in value:
        import capo_sagemaker.types.project_summary_list

        out["ProjectSummaryList"] = (
            capo_sagemaker.types.project_summary_list.serialize_aws_json_1_1(
                value["project_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListProjectsOutput:
    out: ListProjectsOutput = {}  # type: ignore[typeddict-item]
    if "ProjectSummaryList" in data:
        import capo_sagemaker.types.project_summary_list

        out["project_summary_list"] = (
            capo_sagemaker.types.project_summary_list.deserialize_aws_json_1_1(
                data["ProjectSummaryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
