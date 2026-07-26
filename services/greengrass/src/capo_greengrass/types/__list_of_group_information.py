"""Generated from Smithy shape ``com.amazonaws.greengrass#__listOfGroupInformation``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_greengrass.types.group_information

__listOfGroupInformation: TypeAlias = list[
    "capo_greengrass.types.group_information.GroupInformation"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfGroupInformation) -> list:
    import capo_greengrass.types.group_information

    out: list = []
    for item in value:
        out.append(capo_greengrass.types.group_information.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfGroupInformation:
    import capo_greengrass.types.group_information

    out: __listOfGroupInformation = []
    for item in data:
        out.append(capo_greengrass.types.group_information.deserialize_json(item))
    return out
