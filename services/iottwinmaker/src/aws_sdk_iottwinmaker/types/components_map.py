"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ComponentsMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.component_response
    import aws_sdk_iottwinmaker.types.name

ComponentsMap: TypeAlias = dict[
    "aws_sdk_iottwinmaker.types.name.Name",
    "aws_sdk_iottwinmaker.types.component_response.ComponentResponse",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ComponentsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_iottwinmaker.types.component_response

        out[key] = aws_sdk_iottwinmaker.types.component_response.serialize_json(value)
    return out


def deserialize_json(data: dict) -> ComponentsMap:
    out: ComponentsMap = {}
    for key, value in data.items():
        import aws_sdk_iottwinmaker.types.component_response

        out[key] = aws_sdk_iottwinmaker.types.component_response.deserialize_json(value)
    return out
