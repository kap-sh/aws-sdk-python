"""Generated from Smithy shape ``com.amazonaws.codecommit#BatchDisassociateApprovalRuleTemplateFromRepositoriesError``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.error_code
    import aws_sdk_codecommit.types.error_message
    import aws_sdk_codecommit.types.repository_name


class BatchDisassociateApprovalRuleTemplateFromRepositoriesError(TypedDict):
    repository_name: NotRequired[
        "aws_sdk_codecommit.types.repository_name.RepositoryName"
    ]
    """<p>The name of the repository where the association with the template was not able to be removed.</p>"""
    error_code: NotRequired["aws_sdk_codecommit.types.error_code.ErrorCode"]
    """<p>An error code that specifies whether the repository name was not valid or not found.</p>"""
    error_message: NotRequired["aws_sdk_codecommit.types.error_message.ErrorMessage"]
    """<p>An error message that provides details about why the repository name was either not found or not valid.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: BatchDisassociateApprovalRuleTemplateFromRepositoriesError,
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
) -> BatchDisassociateApprovalRuleTemplateFromRepositoriesError:
    out: BatchDisassociateApprovalRuleTemplateFromRepositoriesError = {}  # type: ignore[typeddict-item]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    if "errorCode" in data:
        out["error_code"] = data["errorCode"]
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    return out
