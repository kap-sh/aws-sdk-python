"""Generated from Smithy shape ``com.amazonaws.billingconductor#UpdateTieringInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_billingconductor.errors import DeserializationError

if TYPE_CHECKING:
    import capo_billingconductor.types.update_free_tier_config


class UpdateTieringInput(TypedDict, closed=True):
    free_tier: (
        "capo_billingconductor.types.update_free_tier_config.UpdateFreeTierConfig"
    )
    """<p> The possible Amazon Web Services Free Tier configurations. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTieringInput) -> dict:
    out: dict = {}
    import capo_billingconductor.types.update_free_tier_config

    out["FreeTier"] = (
        capo_billingconductor.types.update_free_tier_config.serialize_json(
            value["free_tier"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateTieringInput:
    out: UpdateTieringInput = {}  # type: ignore[typeddict-item]
    if "FreeTier" in data:
        import capo_billingconductor.types.update_free_tier_config

        out["free_tier"] = (
            capo_billingconductor.types.update_free_tier_config.deserialize_json(
                data["FreeTier"]
            )
        )
    else:
        raise DeserializationError("UpdateTieringInput.free_tier required")
    return out
