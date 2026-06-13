"""Generated from Smithy shape ``com.amazonaws.groundstation#AntennaList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.antenna_list_item

AntennaList: TypeAlias = list[
    "aws_sdk_groundstation.types.antenna_list_item.AntennaListItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: AntennaList) -> list:
    import aws_sdk_groundstation.types.antenna_list_item

    out: list = []
    for item in value:
        out.append(aws_sdk_groundstation.types.antenna_list_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> AntennaList:
    import aws_sdk_groundstation.types.antenna_list_item

    out: AntennaList = []
    for item in data:
        out.append(aws_sdk_groundstation.types.antenna_list_item.deserialize_json(item))
    return out
