"""Generated from Smithy shape ``com.amazonaws.networkmanager#Relationship``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.constrained_string

Relationship = TypedDict(
    "Relationship",
    {
        "from": NotRequired[
            "capo_networkmanager.types.constrained_string.ConstrainedString"
        ],
        "to": NotRequired[
            "capo_networkmanager.types.constrained_string.ConstrainedString"
        ],
    },
    closed=True,
)


# --- restJson1 ser/de ---
def serialize_json(value: Relationship) -> dict:
    out: dict = {}
    if "from" in value:
        out["From"] = value["from"]
    if "to" in value:
        out["To"] = value["to"]
    return out


def deserialize_json(data: dict) -> Relationship:
    out: Relationship = {}  # type: ignore[typeddict-item]
    if "From" in data:
        out["from"] = data["From"]
    if "To" in data:
        out["to"] = data["To"]
    return out
