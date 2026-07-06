"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeCodeRepositoryOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.code_repository_arn
    import aws_sdk_sagemaker.types.creation_time
    import aws_sdk_sagemaker.types.entity_name
    import aws_sdk_sagemaker.types.git_config
    import aws_sdk_sagemaker.types.last_modified_time


class DescribeCodeRepositoryOutput(TypedDict, closed=True):
    code_repository_name: NotRequired["aws_sdk_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the Git repository.</p>"""
    code_repository_arn: NotRequired[
        "aws_sdk_sagemaker.types.code_repository_arn.CodeRepositoryArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the Git repository.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.creation_time.CreationTime"]
    """<p>The date and time that the repository was created.</p>"""
    last_modified_time: NotRequired[
        "aws_sdk_sagemaker.types.last_modified_time.LastModifiedTime"
    ]
    """<p>The date and time that the repository was last changed.</p>"""
    git_config: NotRequired["aws_sdk_sagemaker.types.git_config.GitConfig"]
    """<p>Configuration details about the repository, including the URL where the repository is located, the default branch, and the Amazon Resource Name (ARN) of the Amazon Web Services Secrets Manager secret that contains the credentials used to access the repository.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCodeRepositoryOutput) -> dict:
    out: dict = {}
    if "code_repository_name" in value:
        out["CodeRepositoryName"] = value["code_repository_name"]
    if "code_repository_arn" in value:
        out["CodeRepositoryArn"] = value["code_repository_arn"]
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.creation_time

        out["CreationTime"] = (
            aws_sdk_sagemaker.types.creation_time.serialize_aws_json_1_1(
                value["creation_time"]
            )
        )
    if "last_modified_time" in value:
        import aws_sdk_sagemaker.types.last_modified_time

        out["LastModifiedTime"] = (
            aws_sdk_sagemaker.types.last_modified_time.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "git_config" in value:
        import aws_sdk_sagemaker.types.git_config

        out["GitConfig"] = aws_sdk_sagemaker.types.git_config.serialize_aws_json_1_1(
            value["git_config"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCodeRepositoryOutput:
    out: DescribeCodeRepositoryOutput = {}  # type: ignore[typeddict-item]
    if "CodeRepositoryName" in data:
        out["code_repository_name"] = data["CodeRepositoryName"]
    if "CodeRepositoryArn" in data:
        out["code_repository_arn"] = data["CodeRepositoryArn"]
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.creation_time

        out["creation_time"] = (
            aws_sdk_sagemaker.types.creation_time.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_sagemaker.types.last_modified_time

        out["last_modified_time"] = (
            aws_sdk_sagemaker.types.last_modified_time.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "GitConfig" in data:
        import aws_sdk_sagemaker.types.git_config

        out["git_config"] = aws_sdk_sagemaker.types.git_config.deserialize_aws_json_1_1(
            data["GitConfig"]
        )
    return out
