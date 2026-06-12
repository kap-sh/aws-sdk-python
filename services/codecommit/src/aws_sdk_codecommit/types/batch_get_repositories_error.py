"""Generated from Smithy shape ``com.amazonaws.codecommit#BatchGetRepositoriesError``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.batch_get_repositories_error_code_enum
    import aws_sdk_codecommit.types.error_message
    import aws_sdk_codecommit.types.repository_id
    import aws_sdk_codecommit.types.repository_name


class BatchGetRepositoriesError(TypedDict):
    repository_id: NotRequired["aws_sdk_codecommit.types.repository_id.RepositoryId"]
    """<p>The ID of a repository that either could not be found or was not in a valid state.</p>"""
    repository_name: NotRequired[
        "aws_sdk_codecommit.types.repository_name.RepositoryName"
    ]
    """<p>The name of a repository that either could not be found or was not in a valid state.</p>"""
    error_code: NotRequired[
        "aws_sdk_codecommit.types.batch_get_repositories_error_code_enum.BatchGetRepositoriesErrorCodeEnum"
    ]
    """<p>An error code that specifies the type of failure.</p>"""
    error_message: NotRequired["aws_sdk_codecommit.types.error_message.ErrorMessage"]
    """<p>An error message that provides detail about why the repository either was not found or was not in a valid state.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetRepositoriesError) -> dict:
    out: dict = {}
    if "repository_id" in value:
        out["repositoryId"] = value["repository_id"]
    if "repository_name" in value:
        out["repositoryName"] = value["repository_name"]
    if "error_code" in value:
        import aws_sdk_codecommit.types.batch_get_repositories_error_code_enum

        out["errorCode"] = (
            aws_sdk_codecommit.types.batch_get_repositories_error_code_enum.serialize_aws_json_1_1(
                value["error_code"]
            )
        )
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetRepositoriesError:
    out: BatchGetRepositoriesError = {}  # type: ignore[typeddict-item]
    if "repositoryId" in data:
        out["repository_id"] = data["repositoryId"]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    if "errorCode" in data:
        import aws_sdk_codecommit.types.batch_get_repositories_error_code_enum

        out["error_code"] = (
            aws_sdk_codecommit.types.batch_get_repositories_error_code_enum.deserialize_aws_json_1_1(
                data["errorCode"]
            )
        )
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    return out
