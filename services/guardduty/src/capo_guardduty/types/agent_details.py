"""Generated from Smithy shape ``com.amazonaws.guardduty#AgentDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.string


class AgentDetails(TypedDict, closed=True):
    version: NotRequired["capo_guardduty.types.string.String"]
    """<p>Version of the installed GuardDuty security agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentDetails) -> dict:
    out: dict = {}
    if "version" in value:
        out["version"] = value["version"]
    return out


def deserialize_json(data: dict) -> AgentDetails:
    out: AgentDetails = {}  # type: ignore[typeddict-item]
    if "version" in data:
        out["version"] = data["version"]
    return out
