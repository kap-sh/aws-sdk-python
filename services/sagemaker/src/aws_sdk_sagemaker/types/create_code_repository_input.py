"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateCodeRepositoryInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.entity_name
    import aws_sdk_sagemaker.types.git_config
    import aws_sdk_sagemaker.types.tag_list


class CreateCodeRepositoryInput(TypedDict):
    code_repository_name: NotRequired["aws_sdk_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the Git repository. The name must have 1 to 63 characters. Valid characters are a-z, A-Z, 0-9, and - (hyphen).</p>"""
    git_config: NotRequired["aws_sdk_sagemaker.types.git_config.GitConfig"]
    """<p>Specifies details about the repository, including the URL where the repository is located, the default branch, and credentials to use to access the repository.</p>"""
    tags: NotRequired["aws_sdk_sagemaker.types.tag_list.TagList"]
    """<p>An array of key-value pairs. You can use tags to categorize your Amazon Web Services resources in different ways, for example, by purpose, owner, or environment. For more information, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\">Tagging Amazon Web Services Resources</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateCodeRepositoryInput) -> dict:
    out: dict = {}
    if "code_repository_name" in value:
        out["CodeRepositoryName"] = value["code_repository_name"]
    if "git_config" in value:
        import aws_sdk_sagemaker.types.git_config

        out["GitConfig"] = aws_sdk_sagemaker.types.git_config.serialize_aws_json_1_1(
            value["git_config"]
        )
    if "tags" in value:
        import aws_sdk_sagemaker.types.tag_list

        out["Tags"] = aws_sdk_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateCodeRepositoryInput:
    out: CreateCodeRepositoryInput = {}  # type: ignore[typeddict-item]
    if "CodeRepositoryName" in data:
        out["code_repository_name"] = data["CodeRepositoryName"]
    if "GitConfig" in data:
        import aws_sdk_sagemaker.types.git_config

        out["git_config"] = aws_sdk_sagemaker.types.git_config.deserialize_aws_json_1_1(
            data["GitConfig"]
        )
    if "Tags" in data:
        import aws_sdk_sagemaker.types.tag_list

        out["tags"] = aws_sdk_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
