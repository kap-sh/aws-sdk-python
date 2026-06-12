"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#AccessControls``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_elastic_transcoder.types.access_control

AccessControls: TypeAlias = list[
    "aws_sdk_elastic_transcoder.types.access_control.AccessControl"
]


# --- restJson1 ser/de ---
def serialize_json(value: AccessControls) -> list:
    return list(value)


def deserialize_json(data: list) -> AccessControls:
    return list(data)
