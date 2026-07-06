"""Generated from Smithy shape ``com.amazonaws.devopsagent#RegisteredSlackServiceDetails``."""

from typing_extensions import TypedDict

from aws_sdk_devops_agent.errors import DeserializationError


class RegisteredSlackServiceDetails(TypedDict, closed=True):
    team_id: "str"
    """<p>The Slack team ID.</p>"""
    team_name: "str"
    """<p>The Slack team name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisteredSlackServiceDetails) -> dict:
    out: dict = {}
    out["teamId"] = value["team_id"]
    out["teamName"] = value["team_name"]
    return out


def deserialize_json(data: dict) -> RegisteredSlackServiceDetails:
    out: RegisteredSlackServiceDetails = {}  # type: ignore[typeddict-item]
    if "teamId" in data:
        out["team_id"] = data["teamId"]
    else:
        raise DeserializationError("RegisteredSlackServiceDetails.team_id required")
    if "teamName" in data:
        out["team_name"] = data["teamName"]
    else:
        raise DeserializationError("RegisteredSlackServiceDetails.team_name required")
    return out
