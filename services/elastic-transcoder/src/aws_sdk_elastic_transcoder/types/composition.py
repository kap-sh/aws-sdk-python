"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#Composition``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_elastic_transcoder.types.clip

Composition: TypeAlias = list["aws_sdk_elastic_transcoder.types.clip.Clip"]


# --- restJson1 ser/de ---
def serialize_json(value: Composition) -> list:
    import aws_sdk_elastic_transcoder.types.clip

    out: list = []
    for item in value:
        out.append(aws_sdk_elastic_transcoder.types.clip.serialize_json(item))
    return out


def deserialize_json(data: list) -> Composition:
    import aws_sdk_elastic_transcoder.types.clip

    out: Composition = []
    for item in data:
        out.append(aws_sdk_elastic_transcoder.types.clip.deserialize_json(item))
    return out
