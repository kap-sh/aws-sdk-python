"""Generated from Smithy shape ``com.amazonaws.sagemaker#CodeRepositories``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.code_repository

CodeRepositories: TypeAlias = list[
    "capo_sagemaker.types.code_repository.CodeRepository"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CodeRepositories) -> list:
    import capo_sagemaker.types.code_repository

    out: list = []
    for item in value:
        out.append(capo_sagemaker.types.code_repository.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CodeRepositories:
    import capo_sagemaker.types.code_repository

    out: CodeRepositories = []
    for item in data:
        out.append(capo_sagemaker.types.code_repository.deserialize_aws_json_1_1(item))
    return out
