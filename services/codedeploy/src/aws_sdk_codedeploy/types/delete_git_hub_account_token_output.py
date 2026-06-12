"""Generated from Smithy shape ``com.amazonaws.codedeploy#DeleteGitHubAccountTokenOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.git_hub_account_token_name


class DeleteGitHubAccountTokenOutput(TypedDict):
    token_name: NotRequired[
        "aws_sdk_codedeploy.types.git_hub_account_token_name.GitHubAccountTokenName"
    ]
    """<p>The name of the GitHub account connection that was deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteGitHubAccountTokenOutput) -> dict:
    out: dict = {}
    if "token_name" in value:
        out["tokenName"] = value["token_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteGitHubAccountTokenOutput:
    out: DeleteGitHubAccountTokenOutput = {}  # type: ignore[typeddict-item]
    if "tokenName" in data:
        out["token_name"] = data["tokenName"]
    return out
