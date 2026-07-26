"""Generated from Smithy shape ``com.amazonaws.location#ValidateAddressAdditionalFeatureList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_location.types.validate_address_additional_feature

ValidateAddressAdditionalFeatureList: TypeAlias = list[
    "capo_location.types.validate_address_additional_feature.ValidateAddressAdditionalFeature"
]


# --- restJson1 ser/de ---
def serialize_json(value: ValidateAddressAdditionalFeatureList) -> list:
    return list(value)


def deserialize_json(data: list) -> ValidateAddressAdditionalFeatureList:
    return list(data)
