"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateCodeRepositoryOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.code_repository_arn


class CreateCodeRepositoryOutput(TypedDict, closed=True):
    code_repository_arn: NotRequired[
        "capo_sagemaker.types.code_repository_arn.CodeRepositoryArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the new repository.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateCodeRepositoryOutput) -> dict:
    out: dict = {}
    if "code_repository_arn" in value:
        out["CodeRepositoryArn"] = value["code_repository_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateCodeRepositoryOutput:
    out: CreateCodeRepositoryOutput = {}  # type: ignore[typeddict-item]
    if "CodeRepositoryArn" in data:
        out["code_repository_arn"] = data["CodeRepositoryArn"]
    return out
