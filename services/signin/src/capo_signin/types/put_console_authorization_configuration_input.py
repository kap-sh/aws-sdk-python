"""Generated from Smithy shape ``com.amazonaws.signin#PutConsoleAuthorizationConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_signin.types.target_id


class PutConsoleAuthorizationConfigurationInput(TypedDict, closed=True):
    target_id: NotRequired["capo_signin.types.target_id.TargetId"]
    """Target account identifier"""


# --- restJson1 ser/de ---
def serialize_json(value: PutConsoleAuthorizationConfigurationInput) -> dict:
    out: dict = {}
    if "target_id" in value:
        out["targetId"] = value["target_id"]
    return out


def deserialize_json(data: dict) -> PutConsoleAuthorizationConfigurationInput:
    out: PutConsoleAuthorizationConfigurationInput = {}  # type: ignore[typeddict-item]
    if "targetId" in data:
        out["target_id"] = data["targetId"]
    return out
