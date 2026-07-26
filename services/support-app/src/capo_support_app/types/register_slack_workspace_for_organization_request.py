"""Generated from Smithy shape ``com.amazonaws.supportapp#RegisterSlackWorkspaceForOrganizationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_support_app.errors import DeserializationError

if TYPE_CHECKING:
    import capo_support_app.types.team_id


class RegisterSlackWorkspaceForOrganizationRequest(TypedDict, closed=True):
    team_id: "capo_support_app.types.team_id.teamId"
    """<p>The team ID in Slack. This ID uniquely identifies a Slack workspace, such as <code>T012ABCDEFG</code>. Specify the Slack workspace that you want to use for your organization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterSlackWorkspaceForOrganizationRequest) -> dict:
    out: dict = {}
    out["teamId"] = value["team_id"]
    return out


def deserialize_json(data: dict) -> RegisterSlackWorkspaceForOrganizationRequest:
    out: RegisterSlackWorkspaceForOrganizationRequest = {}  # type: ignore[typeddict-item]
    if "teamId" in data:
        out["team_id"] = data["teamId"]
    else:
        raise DeserializationError(
            "RegisterSlackWorkspaceForOrganizationRequest.team_id required"
        )
    return out
