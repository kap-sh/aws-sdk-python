"""Generated from Smithy shape ``com.amazonaws.billingconductor#CreateFreeTierConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_billingconductor.errors import DeserializationError

if TYPE_CHECKING:
    import capo_billingconductor.types.tiering_activated


class CreateFreeTierConfig(TypedDict, closed=True):
    activated: "capo_billingconductor.types.tiering_activated.TieringActivated"
    """<p> Activate or deactivate Amazon Web Services Free Tier. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFreeTierConfig) -> dict:
    out: dict = {}
    out["Activated"] = value["activated"]
    return out


def deserialize_json(data: dict) -> CreateFreeTierConfig:
    out: CreateFreeTierConfig = {}  # type: ignore[typeddict-item]
    if "Activated" in data:
        out["activated"] = data["Activated"]
    else:
        raise DeserializationError("CreateFreeTierConfig.activated required")
    return out
