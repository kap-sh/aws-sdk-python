"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#PropertyRequests``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.name
    import aws_sdk_iottwinmaker.types.property_request

PropertyRequests: TypeAlias = dict[
    "aws_sdk_iottwinmaker.types.name.Name",
    "aws_sdk_iottwinmaker.types.property_request.PropertyRequest",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: PropertyRequests) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_iottwinmaker.types.property_request

        out[key] = aws_sdk_iottwinmaker.types.property_request.serialize_json(value)
    return out


def deserialize_json(data: dict) -> PropertyRequests:
    out: PropertyRequests = {}
    for key, value in data.items():
        import aws_sdk_iottwinmaker.types.property_request

        out[key] = aws_sdk_iottwinmaker.types.property_request.deserialize_json(value)
    return out
