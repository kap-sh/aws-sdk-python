"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeleteCodeRepositoryInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.entity_name


class DeleteCodeRepositoryInput(TypedDict, closed=True):
    code_repository_name: NotRequired["aws_sdk_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the Git repository to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteCodeRepositoryInput) -> dict:
    out: dict = {}
    if "code_repository_name" in value:
        out["CodeRepositoryName"] = value["code_repository_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteCodeRepositoryInput:
    out: DeleteCodeRepositoryInput = {}  # type: ignore[typeddict-item]
    if "CodeRepositoryName" in data:
        out["code_repository_name"] = data["CodeRepositoryName"]
    return out
