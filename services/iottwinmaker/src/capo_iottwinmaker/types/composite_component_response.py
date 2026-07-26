"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#CompositeComponentResponse``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iottwinmaker.types.component_summary
    import capo_iottwinmaker.types.name

CompositeComponentResponse: TypeAlias = dict[
    "capo_iottwinmaker.types.name.Name",
    "capo_iottwinmaker.types.component_summary.ComponentSummary",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: CompositeComponentResponse) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_iottwinmaker.types.component_summary

        out[key] = capo_iottwinmaker.types.component_summary.serialize_json(value)
    return out


def deserialize_json(data: dict) -> CompositeComponentResponse:
    out: CompositeComponentResponse = {}
    for key, value in data.items():
        import capo_iottwinmaker.types.component_summary

        out[key] = capo_iottwinmaker.types.component_summary.deserialize_json(value)
    return out
