"""Generated from Smithy shape ``com.amazonaws.devopsagent#OAuthAdditionalStepDetails``."""

from typing import TypedDict

from aws_sdk_devops_agent.errors import DeserializationError


class OAuthAdditionalStepDetails(TypedDict):
    authorization_url: "str"
    """<p>The URL to redirect the user to for OAuth authorization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OAuthAdditionalStepDetails) -> dict:
    out: dict = {}
    out["authorizationUrl"] = value["authorization_url"]
    return out


def deserialize_json(data: dict) -> OAuthAdditionalStepDetails:
    out: OAuthAdditionalStepDetails = {}  # type: ignore[typeddict-item]
    if "authorizationUrl" in data:
        out["authorization_url"] = data["authorizationUrl"]
    else:
        raise DeserializationError(
            "OAuthAdditionalStepDetails.authorization_url required"
        )
    return out
