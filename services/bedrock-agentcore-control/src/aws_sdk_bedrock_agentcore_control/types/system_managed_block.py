"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#SystemManagedBlock``."""

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError


class SystemManagedBlock(TypedDict, closed=True):
    managed_by: "str"
    """<p>The identifier of the system or process that manages this rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SystemManagedBlock) -> dict:
    out: dict = {}
    out["managedBy"] = value["managed_by"]
    return out


def deserialize_json(data: dict) -> SystemManagedBlock:
    out: SystemManagedBlock = {}  # type: ignore[typeddict-item]
    if "managedBy" in data:
        out["managed_by"] = data["managedBy"]
    else:
        raise DeserializationError("SystemManagedBlock.managed_by required")
    return out
