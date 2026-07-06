"""Generated from Smithy shape ``com.amazonaws.finspace#PortRange``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace.types.port

PortRange = TypedDict(
    "PortRange",
    {
        "from": "aws_sdk_finspace.types.port.Port",
        "to": "aws_sdk_finspace.types.port.Port",
    },
    closed=True,
)


# --- restJson1 ser/de ---
def serialize_json(value: PortRange) -> dict:
    out: dict = {}
    out["from"] = value.get("from", 0)
    out["to"] = value.get("to", 0)
    return out


def deserialize_json(data: dict) -> PortRange:
    out: PortRange = {}  # type: ignore[typeddict-item]
    if "from" in data:
        out["from"] = data["from"]
    else:
        out["from"] = 0
    if "to" in data:
        out["to"] = data["to"]
    else:
        out["to"] = 0
    return out
