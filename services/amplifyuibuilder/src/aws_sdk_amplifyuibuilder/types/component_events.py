"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ComponentEvents``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.component_event

ComponentEvents: TypeAlias = dict[
    "str", "aws_sdk_amplifyuibuilder.types.component_event.ComponentEvent"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ComponentEvents) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_amplifyuibuilder.types.component_event

        out[key] = aws_sdk_amplifyuibuilder.types.component_event.serialize_json(value)
    return out


def deserialize_json(data: dict) -> ComponentEvents:
    out: ComponentEvents = {}
    for key, value in data.items():
        import aws_sdk_amplifyuibuilder.types.component_event

        out[key] = aws_sdk_amplifyuibuilder.types.component_event.deserialize_json(
            value
        )
    return out
