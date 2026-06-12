"""Generated from Smithy shape ``com.amazonaws.connectcampaigns#AgentlessDialerConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connectcampaigns.types.dialing_capacity


class AgentlessDialerConfig(TypedDict):
    dialing_capacity: NotRequired[
        "aws_sdk_connectcampaigns.types.dialing_capacity.DialingCapacity"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: AgentlessDialerConfig) -> dict:
    out: dict = {}
    if "dialing_capacity" in value:
        out["dialingCapacity"] = value["dialing_capacity"]
    return out


def deserialize_json(data: dict) -> AgentlessDialerConfig:
    out: AgentlessDialerConfig = {}  # type: ignore[typeddict-item]
    if "dialingCapacity" in data:
        out["dialing_capacity"] = data["dialingCapacity"]
    return out
