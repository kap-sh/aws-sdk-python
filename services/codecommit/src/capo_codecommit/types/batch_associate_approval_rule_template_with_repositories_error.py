"""Generated from Smithy shape ``com.amazonaws.codecommit#BatchAssociateApprovalRuleTemplateWithRepositoriesError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.error_code
    import capo_codecommit.types.error_message
    import capo_codecommit.types.repository_name


class BatchAssociateApprovalRuleTemplateWithRepositoriesError(TypedDict, closed=True):
    repository_name: NotRequired["capo_codecommit.types.repository_name.RepositoryName"]
    """<p>The name of the repository where the association was not made.</p>"""
    error_code: NotRequired["capo_codecommit.types.error_code.ErrorCode"]
    """<p>An error code that specifies whether the repository name was not valid or not found.</p>"""
    error_message: NotRequired["capo_codecommit.types.error_message.ErrorMessage"]
    """<p>An error message that provides details about why the repository name was not found or not valid.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: BatchAssociateApprovalRuleTemplateWithRepositoriesError,
) -> dict:
    out: dict = {}
    if "repository_name" in value:
        out["repositoryName"] = value["repository_name"]
    if "error_code" in value:
        out["errorCode"] = value["error_code"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> BatchAssociateApprovalRuleTemplateWithRepositoriesError:
    out: BatchAssociateApprovalRuleTemplateWithRepositoriesError = {}  # type: ignore[typeddict-item]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    if "errorCode" in data:
        out["error_code"] = data["errorCode"]
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    return out
