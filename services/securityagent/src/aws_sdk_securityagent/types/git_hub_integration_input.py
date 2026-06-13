"""Generated from Smithy shape ``com.amazonaws.securityagent#GitHubIntegrationInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.auth_code
    import aws_sdk_securityagent.types.csrf_state


class GitHubIntegrationInput(TypedDict):
    code: "aws_sdk_securityagent.types.auth_code.AuthCode"
    """<p>The OAuth authorization code received from GitHub.</p>"""
    state: "aws_sdk_securityagent.types.csrf_state.CsrfState"
    """<p>The CSRF state token for validating the OAuth flow.</p>"""
    organization_name: NotRequired["str"]
    """<p>The name of the GitHub organization to integrate with.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GitHubIntegrationInput) -> dict:
    out: dict = {}
    out["code"] = value["code"]
    out["state"] = value["state"]
    if "organization_name" in value:
        out["organizationName"] = value["organization_name"]
    return out


def deserialize_json(data: dict) -> GitHubIntegrationInput:
    out: GitHubIntegrationInput = {}  # type: ignore[typeddict-item]
    if "code" in data:
        out["code"] = data["code"]
    else:
        raise DeserializationError("GitHubIntegrationInput.code required")
    if "state" in data:
        out["state"] = data["state"]
    else:
        raise DeserializationError("GitHubIntegrationInput.state required")
    if "organizationName" in data:
        out["organization_name"] = data["organizationName"]
    return out
