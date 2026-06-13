"""Generated from Smithy shape ``com.amazonaws.neptunedata#LongValuedMapList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_neptunedata.types.long_valued_map

LongValuedMapList: TypeAlias = list[
    "aws_sdk_neptunedata.types.long_valued_map.LongValuedMap"
]


# --- restJson1 ser/de ---
def serialize_json(value: LongValuedMapList) -> list:
    import aws_sdk_neptunedata.types.long_valued_map

    out: list = []
    for item in value:
        out.append(aws_sdk_neptunedata.types.long_valued_map.serialize_json(item))
    return out


def deserialize_json(data: list) -> LongValuedMapList:
    import aws_sdk_neptunedata.types.long_valued_map

    out: LongValuedMapList = []
    for item in data:
        out.append(aws_sdk_neptunedata.types.long_valued_map.deserialize_json(item))
    return out
