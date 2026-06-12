"""Generated from Smithy shape ``com.amazonaws.finspace#KxDataviewSegmentConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_finspace.types.kx_dataview_segment_configuration

KxDataviewSegmentConfigurationList: TypeAlias = list[
    "aws_sdk_finspace.types.kx_dataview_segment_configuration.KxDataviewSegmentConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: KxDataviewSegmentConfigurationList) -> list:
    import aws_sdk_finspace.types.kx_dataview_segment_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_finspace.types.kx_dataview_segment_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> KxDataviewSegmentConfigurationList:
    import aws_sdk_finspace.types.kx_dataview_segment_configuration

    out: KxDataviewSegmentConfigurationList = []
    for item in data:
        out.append(
            aws_sdk_finspace.types.kx_dataview_segment_configuration.deserialize_json(
                item
            )
        )
    return out
