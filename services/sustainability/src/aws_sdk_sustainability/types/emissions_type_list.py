"""Generated from Smithy shape ``com.amazonaws.sustainability#EmissionsTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sustainability.types.emissions_type

EmissionsTypeList: TypeAlias = list[
    "aws_sdk_sustainability.types.emissions_type.EmissionsType"
]


# --- restJson1 ser/de ---
def serialize_json(value: EmissionsTypeList) -> list:
    import aws_sdk_sustainability.types.emissions_type

    out: list = []
    for item in value:
        out.append(aws_sdk_sustainability.types.emissions_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> EmissionsTypeList:
    import aws_sdk_sustainability.types.emissions_type

    out: EmissionsTypeList = []
    for item in data:
        out.append(aws_sdk_sustainability.types.emissions_type.deserialize_json(item))
    return out
