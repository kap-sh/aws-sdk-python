"""Generated from Smithy shape ``com.amazonaws.greengrass#__listOfVersionInformation``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_greengrass.types.version_information

__listOfVersionInformation: TypeAlias = list[
    "capo_greengrass.types.version_information.VersionInformation"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfVersionInformation) -> list:
    import capo_greengrass.types.version_information

    out: list = []
    for item in value:
        out.append(capo_greengrass.types.version_information.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfVersionInformation:
    import capo_greengrass.types.version_information

    out: __listOfVersionInformation = []
    for item in data:
        out.append(capo_greengrass.types.version_information.deserialize_json(item))
    return out
