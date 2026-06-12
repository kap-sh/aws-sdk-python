"""Generated from Smithy shape ``com.amazonaws.geoplaces#ParsedQuerySecondaryAddressComponentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.parsed_query_secondary_address_component

ParsedQuerySecondaryAddressComponentList: TypeAlias = list[
    "aws_sdk_geo_places.types.parsed_query_secondary_address_component.ParsedQuerySecondaryAddressComponent"
]


# --- restJson1 ser/de ---
def serialize_json(value: ParsedQuerySecondaryAddressComponentList) -> list:
    import aws_sdk_geo_places.types.parsed_query_secondary_address_component

    out: list = []
    for item in value:
        out.append(
            aws_sdk_geo_places.types.parsed_query_secondary_address_component.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ParsedQuerySecondaryAddressComponentList:
    import aws_sdk_geo_places.types.parsed_query_secondary_address_component

    out: ParsedQuerySecondaryAddressComponentList = []
    for item in data:
        out.append(
            aws_sdk_geo_places.types.parsed_query_secondary_address_component.deserialize_json(
                item
            )
        )
    return out
