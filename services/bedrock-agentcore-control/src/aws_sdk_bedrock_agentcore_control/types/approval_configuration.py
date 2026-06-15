"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ApprovalConfiguration``."""

from typing import TypedDict


class ApprovalConfiguration(TypedDict):
    auto_approval: "bool"
    """<p>Whether registry records are auto-approved. When set to <code>true</code>, records are automatically approved upon creation. When set to <code>false</code> (the default), records require explicit approval for security purposes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApprovalConfiguration) -> dict:
    out: dict = {}
    out["autoApproval"] = value.get("auto_approval", False)
    return out


def deserialize_json(data: dict) -> ApprovalConfiguration:
    out: ApprovalConfiguration = {}  # type: ignore[typeddict-item]
    if "autoApproval" in data:
        out["auto_approval"] = data["autoApproval"]
    else:
        out["auto_approval"] = False
    return out
