"""Generated from Smithy shape ``com.amazonaws.panorama#AlternateSoftwares``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_panorama.types.alternate_software_metadata

AlternateSoftwares: TypeAlias = list[
    "capo_panorama.types.alternate_software_metadata.AlternateSoftwareMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: AlternateSoftwares) -> list:
    import capo_panorama.types.alternate_software_metadata

    out: list = []
    for item in value:
        out.append(capo_panorama.types.alternate_software_metadata.serialize_json(item))
    return out


def deserialize_json(data: list) -> AlternateSoftwares:
    import capo_panorama.types.alternate_software_metadata

    out: AlternateSoftwares = []
    for item in data:
        out.append(
            capo_panorama.types.alternate_software_metadata.deserialize_json(item)
        )
    return out
