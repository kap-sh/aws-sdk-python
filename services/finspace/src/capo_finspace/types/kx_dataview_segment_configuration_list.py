"""Generated from Smithy shape ``com.amazonaws.finspace#KxDataviewSegmentConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_finspace.types.kx_dataview_segment_configuration

KxDataviewSegmentConfigurationList: TypeAlias = list[
    "capo_finspace.types.kx_dataview_segment_configuration.KxDataviewSegmentConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: KxDataviewSegmentConfigurationList) -> list:
    import capo_finspace.types.kx_dataview_segment_configuration

    out: list = []
    for item in value:
        out.append(
            capo_finspace.types.kx_dataview_segment_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> KxDataviewSegmentConfigurationList:
    import capo_finspace.types.kx_dataview_segment_configuration

    out: KxDataviewSegmentConfigurationList = []
    for item in data:
        out.append(
            capo_finspace.types.kx_dataview_segment_configuration.deserialize_json(item)
        )
    return out
