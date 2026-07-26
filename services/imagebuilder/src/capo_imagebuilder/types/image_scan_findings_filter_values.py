"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ImageScanFindingsFilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_imagebuilder.types.filter_value

ImageScanFindingsFilterValues: TypeAlias = list[
    "capo_imagebuilder.types.filter_value.FilterValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: ImageScanFindingsFilterValues) -> list:
    return list(value)


def deserialize_json(data: list) -> ImageScanFindingsFilterValues:
    return list(data)
