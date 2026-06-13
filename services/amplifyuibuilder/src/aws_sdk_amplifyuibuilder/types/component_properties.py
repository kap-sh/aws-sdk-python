"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ComponentProperties``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.component_property

ComponentProperties: TypeAlias = dict[
    "str", "aws_sdk_amplifyuibuilder.types.component_property.ComponentProperty"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ComponentProperties) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_amplifyuibuilder.types.component_property

        out[key] = aws_sdk_amplifyuibuilder.types.component_property.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> ComponentProperties:
    out: ComponentProperties = {}
    for key, value in data.items():
        import aws_sdk_amplifyuibuilder.types.component_property

        out[key] = aws_sdk_amplifyuibuilder.types.component_property.deserialize_json(
            value
        )
    return out
