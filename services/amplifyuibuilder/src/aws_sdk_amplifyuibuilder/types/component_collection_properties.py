"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ComponentCollectionProperties``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.component_data_configuration

ComponentCollectionProperties: TypeAlias = dict[
    "str",
    "aws_sdk_amplifyuibuilder.types.component_data_configuration.ComponentDataConfiguration",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ComponentCollectionProperties) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_amplifyuibuilder.types.component_data_configuration

        out[key] = (
            aws_sdk_amplifyuibuilder.types.component_data_configuration.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> ComponentCollectionProperties:
    out: ComponentCollectionProperties = {}
    for key, value in data.items():
        import aws_sdk_amplifyuibuilder.types.component_data_configuration

        out[key] = (
            aws_sdk_amplifyuibuilder.types.component_data_configuration.deserialize_json(
                value
            )
        )
    return out
