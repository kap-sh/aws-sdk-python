"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ComponentsMapRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.component_request
    import aws_sdk_iottwinmaker.types.name

ComponentsMapRequest: TypeAlias = dict[
    "aws_sdk_iottwinmaker.types.name.Name",
    "aws_sdk_iottwinmaker.types.component_request.ComponentRequest",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ComponentsMapRequest) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_iottwinmaker.types.component_request

        out[key] = aws_sdk_iottwinmaker.types.component_request.serialize_json(value)
    return out


def deserialize_json(data: dict) -> ComponentsMapRequest:
    out: ComponentsMapRequest = {}
    for key, value in data.items():
        import aws_sdk_iottwinmaker.types.component_request

        out[key] = aws_sdk_iottwinmaker.types.component_request.deserialize_json(value)
    return out
