"""Generated from Smithy shape ``com.amazonaws.supportapp#DeleteSlackWorkspaceConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_support_app.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_support_app.types.team_id


class DeleteSlackWorkspaceConfigurationRequest(TypedDict):
    team_id: "aws_sdk_support_app.types.team_id.teamId"
    """<p>The team ID in Slack. This ID uniquely identifies a Slack workspace, such as <code>T012ABCDEFG</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSlackWorkspaceConfigurationRequest) -> dict:
    out: dict = {}
    out["teamId"] = value["team_id"]
    return out


def deserialize_json(data: dict) -> DeleteSlackWorkspaceConfigurationRequest:
    out: DeleteSlackWorkspaceConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "teamId" in data:
        out["team_id"] = data["teamId"]
    else:
        raise DeserializationError(
            "DeleteSlackWorkspaceConfigurationRequest.team_id required"
        )
    return out
