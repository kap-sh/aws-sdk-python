"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#ConcatenationSourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.concatenation_source

ConcatenationSourceList: TypeAlias = list[
    "aws_sdk_chime_sdk_media_pipelines.types.concatenation_source.ConcatenationSource"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConcatenationSourceList) -> list:
    import aws_sdk_chime_sdk_media_pipelines.types.concatenation_source

    out: list = []
    for item in value:
        out.append(
            aws_sdk_chime_sdk_media_pipelines.types.concatenation_source.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ConcatenationSourceList:
    import aws_sdk_chime_sdk_media_pipelines.types.concatenation_source

    out: ConcatenationSourceList = []
    for item in data:
        out.append(
            aws_sdk_chime_sdk_media_pipelines.types.concatenation_source.deserialize_json(
                item
            )
        )
    return out
