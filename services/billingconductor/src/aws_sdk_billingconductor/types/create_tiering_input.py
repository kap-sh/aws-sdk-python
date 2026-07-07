"""Generated from Smithy shape ``com.amazonaws.billingconductor#CreateTieringInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_billingconductor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.create_free_tier_config


class CreateTieringInput(TypedDict, closed=True):
    free_tier: (
        "aws_sdk_billingconductor.types.create_free_tier_config.CreateFreeTierConfig"
    )
    """<p> The possible Amazon Web Services Free Tier configurations. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTieringInput) -> dict:
    out: dict = {}
    import aws_sdk_billingconductor.types.create_free_tier_config

    out["FreeTier"] = (
        aws_sdk_billingconductor.types.create_free_tier_config.serialize_json(
            value["free_tier"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateTieringInput:
    out: CreateTieringInput = {}  # type: ignore[typeddict-item]
    if "FreeTier" in data:
        import aws_sdk_billingconductor.types.create_free_tier_config

        out["free_tier"] = (
            aws_sdk_billingconductor.types.create_free_tier_config.deserialize_json(
                data["FreeTier"]
            )
        )
    else:
        raise DeserializationError("CreateTieringInput.free_tier required")
    return out
