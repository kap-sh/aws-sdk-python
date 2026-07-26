"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#PricingBundles``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iottwinmaker.types.bundle_name

PricingBundles: TypeAlias = list["capo_iottwinmaker.types.bundle_name.BundleName"]


# --- restJson1 ser/de ---
def serialize_json(value: PricingBundles) -> list:
    return list(value)


def deserialize_json(data: list) -> PricingBundles:
    return list(data)
