"""Generated from Smithy shape ``com.amazonaws.billingconductor#Tiering``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_billingconductor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.free_tier_config


class Tiering(TypedDict):
    free_tier: "aws_sdk_billingconductor.types.free_tier_config.FreeTierConfig"
    """<p> The possible Amazon Web Services Free Tier configurations. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Tiering) -> dict:
    out: dict = {}
    import aws_sdk_billingconductor.types.free_tier_config

    out["FreeTier"] = aws_sdk_billingconductor.types.free_tier_config.serialize_json(
        value["free_tier"]
    )
    return out


def deserialize_json(data: dict) -> Tiering:
    out: Tiering = {}  # type: ignore[typeddict-item]
    if "FreeTier" in data:
        import aws_sdk_billingconductor.types.free_tier_config

        out["free_tier"] = (
            aws_sdk_billingconductor.types.free_tier_config.deserialize_json(
                data["FreeTier"]
            )
        )
    else:
        raise DeserializationError("Tiering.free_tier required")
    return out
