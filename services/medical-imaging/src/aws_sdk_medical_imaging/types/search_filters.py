"""Generated from Smithy shape ``com.amazonaws.medicalimaging#SearchFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medical_imaging.types.search_filter

SearchFilters: TypeAlias = list[
    "aws_sdk_medical_imaging.types.search_filter.SearchFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchFilters) -> list:
    import aws_sdk_medical_imaging.types.search_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_medical_imaging.types.search_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> SearchFilters:
    import aws_sdk_medical_imaging.types.search_filter

    out: SearchFilters = []
    for item in data:
        out.append(aws_sdk_medical_imaging.types.search_filter.deserialize_json(item))
    return out
