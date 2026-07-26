"""Generated from Smithy shape ``com.amazonaws.inspector2#UpdateGitLabSelfManagedIntegrationDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector2.types.git_lab_auth_code


class UpdateGitLabSelfManagedIntegrationDetail(TypedDict, closed=True):
    auth_code: "capo_inspector2.types.git_lab_auth_code.GitLabAuthCode"
    """<p>The authorization code received from the self-managed GitLab instance to update the integration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGitLabSelfManagedIntegrationDetail) -> dict:
    out: dict = {}
    out["authCode"] = value["auth_code"]
    return out


def deserialize_json(data: dict) -> UpdateGitLabSelfManagedIntegrationDetail:
    out: UpdateGitLabSelfManagedIntegrationDetail = {}  # type: ignore[typeddict-item]
    if "authCode" in data:
        out["auth_code"] = data["authCode"]
    else:
        raise DeserializationError(
            "UpdateGitLabSelfManagedIntegrationDetail.auth_code required"
        )
    return out
