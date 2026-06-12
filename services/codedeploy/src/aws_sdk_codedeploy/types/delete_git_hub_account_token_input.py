"""Generated from Smithy shape ``com.amazonaws.codedeploy#DeleteGitHubAccountTokenInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.git_hub_account_token_name


class DeleteGitHubAccountTokenInput(TypedDict):
    token_name: NotRequired[
        "aws_sdk_codedeploy.types.git_hub_account_token_name.GitHubAccountTokenName"
    ]
    """<p>The name of the GitHub account connection to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteGitHubAccountTokenInput) -> dict:
    out: dict = {}
    if "token_name" in value:
        out["tokenName"] = value["token_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteGitHubAccountTokenInput:
    out: DeleteGitHubAccountTokenInput = {}  # type: ignore[typeddict-item]
    if "tokenName" in data:
        out["token_name"] = data["tokenName"]
    return out
