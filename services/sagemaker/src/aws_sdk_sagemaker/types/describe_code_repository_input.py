"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeCodeRepositoryInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.entity_name


class DescribeCodeRepositoryInput(TypedDict):
    code_repository_name: NotRequired["aws_sdk_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the Git repository to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCodeRepositoryInput) -> dict:
    out: dict = {}
    if "code_repository_name" in value:
        out["CodeRepositoryName"] = value["code_repository_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCodeRepositoryInput:
    out: DescribeCodeRepositoryInput = {}  # type: ignore[typeddict-item]
    if "CodeRepositoryName" in data:
        out["code_repository_name"] = data["CodeRepositoryName"]
    return out
