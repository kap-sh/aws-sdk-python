"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ComponentOverrides``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.component_overrides_value

ComponentOverrides: TypeAlias = dict[
    "str",
    "aws_sdk_amplifyuibuilder.types.component_overrides_value.ComponentOverridesValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ComponentOverrides) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_amplifyuibuilder.types.component_overrides_value

        out[key] = (
            aws_sdk_amplifyuibuilder.types.component_overrides_value.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> ComponentOverrides:
    out: ComponentOverrides = {}
    for key, value in data.items():
        import aws_sdk_amplifyuibuilder.types.component_overrides_value

        out[key] = (
            aws_sdk_amplifyuibuilder.types.component_overrides_value.deserialize_json(
                value
            )
        )
    return out
