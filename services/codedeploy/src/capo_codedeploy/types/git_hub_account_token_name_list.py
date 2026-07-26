"""Generated from Smithy shape ``com.amazonaws.codedeploy#GitHubAccountTokenNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codedeploy.types.git_hub_account_token_name

GitHubAccountTokenNameList: TypeAlias = list[
    "capo_codedeploy.types.git_hub_account_token_name.GitHubAccountTokenName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GitHubAccountTokenNameList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> GitHubAccountTokenNameList:
    return list(data)
