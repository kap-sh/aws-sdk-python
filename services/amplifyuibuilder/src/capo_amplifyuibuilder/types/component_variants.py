"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ComponentVariants``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.component_variant

ComponentVariants: TypeAlias = list[
    "capo_amplifyuibuilder.types.component_variant.ComponentVariant"
]


# --- restJson1 ser/de ---
def serialize_json(value: ComponentVariants) -> list:
    import capo_amplifyuibuilder.types.component_variant

    out: list = []
    for item in value:
        out.append(capo_amplifyuibuilder.types.component_variant.serialize_json(item))
    return out


def deserialize_json(data: list) -> ComponentVariants:
    import capo_amplifyuibuilder.types.component_variant

    out: ComponentVariants = []
    for item in data:
        out.append(capo_amplifyuibuilder.types.component_variant.deserialize_json(item))
    return out
