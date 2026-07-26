"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListCodeRepositoriesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.code_repository_summary_list
    import capo_sagemaker.types.next_token


class ListCodeRepositoriesOutput(TypedDict, closed=True):
    code_repository_summary_list: NotRequired[
        "capo_sagemaker.types.code_repository_summary_list.CodeRepositorySummaryList"
    ]
    """<p>Gets a list of summaries of the Git repositories. Each summary specifies the following values for the repository: </p> <ul> <li> <p>Name</p> </li> <li> <p>Amazon Resource Name (ARN)</p> </li> <li> <p>Creation time</p> </li> <li> <p>Last modified time</p> </li> <li> <p>Configuration information, including the URL location of the repository and the ARN of the Amazon Web Services Secrets Manager secret that contains the credentials used to access the repository.</p> </li> </ul>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>If the result of a <code>ListCodeRepositoriesOutput</code> request was truncated, the response includes a <code>NextToken</code>. To get the next set of Git repositories, use the token in the next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCodeRepositoriesOutput) -> dict:
    out: dict = {}
    if "code_repository_summary_list" in value:
        import capo_sagemaker.types.code_repository_summary_list

        out["CodeRepositorySummaryList"] = (
            capo_sagemaker.types.code_repository_summary_list.serialize_aws_json_1_1(
                value["code_repository_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCodeRepositoriesOutput:
    out: ListCodeRepositoriesOutput = {}  # type: ignore[typeddict-item]
    if "CodeRepositorySummaryList" in data:
        import capo_sagemaker.types.code_repository_summary_list

        out["code_repository_summary_list"] = (
            capo_sagemaker.types.code_repository_summary_list.deserialize_aws_json_1_1(
                data["CodeRepositorySummaryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
