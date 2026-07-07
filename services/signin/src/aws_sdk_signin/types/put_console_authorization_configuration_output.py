"""Generated from Smithy shape ``com.amazonaws.signin#PutConsoleAuthorizationConfigurationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_signin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_signin.types.target_id


class PutConsoleAuthorizationConfigurationOutput(TypedDict, closed=True):
    target_id: "aws_sdk_signin.types.target_id.TargetId"
    """Target account identifier"""
    scope: "str"
    """Authorization scope"""
    console_authorization_enabled: "bool"
    """Whether console authorization is enabled"""


# --- restJson1 ser/de ---
def serialize_json(value: PutConsoleAuthorizationConfigurationOutput) -> dict:
    out: dict = {}
    out["targetId"] = value["target_id"]
    out["scope"] = value["scope"]
    out["consoleAuthorizationEnabled"] = value["console_authorization_enabled"]
    return out


def deserialize_json(data: dict) -> PutConsoleAuthorizationConfigurationOutput:
    out: PutConsoleAuthorizationConfigurationOutput = {}  # type: ignore[typeddict-item]
    if "targetId" in data:
        out["target_id"] = data["targetId"]
    else:
        raise DeserializationError(
            "PutConsoleAuthorizationConfigurationOutput.target_id required"
        )
    if "scope" in data:
        out["scope"] = data["scope"]
    else:
        raise DeserializationError(
            "PutConsoleAuthorizationConfigurationOutput.scope required"
        )
    if "consoleAuthorizationEnabled" in data:
        out["console_authorization_enabled"] = data["consoleAuthorizationEnabled"]
    else:
        raise DeserializationError(
            "PutConsoleAuthorizationConfigurationOutput.console_authorization_enabled required"
        )
    return out
