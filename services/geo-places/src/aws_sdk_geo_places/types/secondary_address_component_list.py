"""Generated from Smithy shape ``com.amazonaws.geoplaces#SecondaryAddressComponentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.secondary_address_component

SecondaryAddressComponentList: TypeAlias = list[
    "aws_sdk_geo_places.types.secondary_address_component.SecondaryAddressComponent"
]


# --- restJson1 ser/de ---
def serialize_json(value: SecondaryAddressComponentList) -> list:
    import aws_sdk_geo_places.types.secondary_address_component

    out: list = []
    for item in value:
        out.append(
            aws_sdk_geo_places.types.secondary_address_component.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SecondaryAddressComponentList:
    import aws_sdk_geo_places.types.secondary_address_component

    out: SecondaryAddressComponentList = []
    for item in data:
        out.append(
            aws_sdk_geo_places.types.secondary_address_component.deserialize_json(item)
        )
    return out
