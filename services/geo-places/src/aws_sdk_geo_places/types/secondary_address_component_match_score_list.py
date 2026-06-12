"""Generated from Smithy shape ``com.amazonaws.geoplaces#SecondaryAddressComponentMatchScoreList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.secondary_address_component_match_score

SecondaryAddressComponentMatchScoreList: TypeAlias = list[
    "aws_sdk_geo_places.types.secondary_address_component_match_score.SecondaryAddressComponentMatchScore"
]


# --- restJson1 ser/de ---
def serialize_json(value: SecondaryAddressComponentMatchScoreList) -> list:
    import aws_sdk_geo_places.types.secondary_address_component_match_score

    out: list = []
    for item in value:
        out.append(
            aws_sdk_geo_places.types.secondary_address_component_match_score.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SecondaryAddressComponentMatchScoreList:
    import aws_sdk_geo_places.types.secondary_address_component_match_score

    out: SecondaryAddressComponentMatchScoreList = []
    for item in data:
        out.append(
            aws_sdk_geo_places.types.secondary_address_component_match_score.deserialize_json(
                item
            )
        )
    return out
