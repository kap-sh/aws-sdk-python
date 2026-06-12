"""Generated from Smithy shape ``com.amazonaws.medialive#FailedMediaResourceMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.media_resource

FailedMediaResourceMap: TypeAlias = dict[
    "aws_sdk_medialive.types.__string.__string",
    "aws_sdk_medialive.types.media_resource.MediaResource",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: FailedMediaResourceMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_medialive.types.media_resource

        out[key] = aws_sdk_medialive.types.media_resource.serialize_json(value)
    return out


def deserialize_json(data: dict) -> FailedMediaResourceMap:
    out: FailedMediaResourceMap = {}
    for key, value in data.items():
        import aws_sdk_medialive.types.media_resource

        out[key] = aws_sdk_medialive.types.media_resource.deserialize_json(value)
    return out
