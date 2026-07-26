"""Generated from Smithy shape ``com.amazonaws.socialmessaging#MetaLibraryTemplatesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_socialmessaging.types.meta_library_template_definition

MetaLibraryTemplatesList: TypeAlias = list[
    "capo_socialmessaging.types.meta_library_template_definition.MetaLibraryTemplateDefinition"
]


# --- restJson1 ser/de ---
def serialize_json(value: MetaLibraryTemplatesList) -> list:
    import capo_socialmessaging.types.meta_library_template_definition

    out: list = []
    for item in value:
        out.append(
            capo_socialmessaging.types.meta_library_template_definition.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> MetaLibraryTemplatesList:
    import capo_socialmessaging.types.meta_library_template_definition

    out: MetaLibraryTemplatesList = []
    for item in data:
        out.append(
            capo_socialmessaging.types.meta_library_template_definition.deserialize_json(
                item
            )
        )
    return out
