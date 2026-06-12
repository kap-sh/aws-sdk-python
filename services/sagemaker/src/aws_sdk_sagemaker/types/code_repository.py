"""Generated from Smithy shape ``com.amazonaws.sagemaker#CodeRepository``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.repository_url


class CodeRepository(TypedDict):
    repository_url: NotRequired["aws_sdk_sagemaker.types.repository_url.RepositoryUrl"]
    """<p>The URL of the Git repository.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CodeRepository) -> dict:
    out: dict = {}
    if "repository_url" in value:
        out["RepositoryUrl"] = value["repository_url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CodeRepository:
    out: CodeRepository = {}  # type: ignore[typeddict-item]
    if "RepositoryUrl" in data:
        out["repository_url"] = data["RepositoryUrl"]
    return out
