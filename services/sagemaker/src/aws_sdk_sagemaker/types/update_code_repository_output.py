"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateCodeRepositoryOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.code_repository_arn


class UpdateCodeRepositoryOutput(TypedDict, closed=True):
    code_repository_arn: NotRequired[
        "aws_sdk_sagemaker.types.code_repository_arn.CodeRepositoryArn"
    ]
    """<p>The ARN of the Git repository.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateCodeRepositoryOutput) -> dict:
    out: dict = {}
    if "code_repository_arn" in value:
        out["CodeRepositoryArn"] = value["code_repository_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateCodeRepositoryOutput:
    out: UpdateCodeRepositoryOutput = {}  # type: ignore[typeddict-item]
    if "CodeRepositoryArn" in data:
        out["code_repository_arn"] = data["CodeRepositoryArn"]
    return out
