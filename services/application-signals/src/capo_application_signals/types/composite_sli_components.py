"""Generated from Smithy shape ``com.amazonaws.applicationsignals#CompositeSliComponents``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_application_signals.types.composite_sli_component

CompositeSliComponents: TypeAlias = list[
    "capo_application_signals.types.composite_sli_component.CompositeSliComponent"
]


# --- restJson1 ser/de ---
def serialize_json(value: CompositeSliComponents) -> list:
    import capo_application_signals.types.composite_sli_component

    out: list = []
    for item in value:
        out.append(
            capo_application_signals.types.composite_sli_component.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CompositeSliComponents:
    import capo_application_signals.types.composite_sli_component

    out: CompositeSliComponents = []
    for item in data:
        out.append(
            capo_application_signals.types.composite_sli_component.deserialize_json(
                item
            )
        )
    return out
