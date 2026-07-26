"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeCodeRepositoryInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.entity_name


class DescribeCodeRepositoryInput(TypedDict, closed=True):
    code_repository_name: NotRequired["capo_sagemaker.types.entity_name.EntityName"]
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
