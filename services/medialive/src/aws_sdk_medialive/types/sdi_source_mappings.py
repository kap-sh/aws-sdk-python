"""Generated from Smithy shape ``com.amazonaws.medialive#SdiSourceMappings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.sdi_source_mapping

SdiSourceMappings: TypeAlias = list[
    "aws_sdk_medialive.types.sdi_source_mapping.SdiSourceMapping"
]


# --- restJson1 ser/de ---
def serialize_json(value: SdiSourceMappings) -> list:
    import aws_sdk_medialive.types.sdi_source_mapping

    out: list = []
    for item in value:
        out.append(aws_sdk_medialive.types.sdi_source_mapping.serialize_json(item))
    return out


def deserialize_json(data: list) -> SdiSourceMappings:
    import aws_sdk_medialive.types.sdi_source_mapping

    out: SdiSourceMappings = []
    for item in data:
        out.append(aws_sdk_medialive.types.sdi_source_mapping.deserialize_json(item))
    return out
