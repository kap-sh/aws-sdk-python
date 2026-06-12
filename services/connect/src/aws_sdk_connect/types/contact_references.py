"""Generated from Smithy shape ``com.amazonaws.connect#ContactReferences``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.reference
    import aws_sdk_connect.types.reference_key

ContactReferences: TypeAlias = dict[
    "aws_sdk_connect.types.reference_key.ReferenceKey",
    "aws_sdk_connect.types.reference.Reference",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ContactReferences) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_connect.types.reference

        out[key] = aws_sdk_connect.types.reference.serialize_json(value)
    return out


def deserialize_json(data: dict) -> ContactReferences:
    out: ContactReferences = {}
    for key, value in data.items():
        import aws_sdk_connect.types.reference

        out[key] = aws_sdk_connect.types.reference.deserialize_json(value)
    return out
