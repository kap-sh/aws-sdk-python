"""Generated from Smithy shape ``com.amazonaws.socialmessaging#MetaLibraryTemplateButtonList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_socialmessaging.types.library_template_button_list

MetaLibraryTemplateButtonList: TypeAlias = list[
    "capo_socialmessaging.types.library_template_button_list.LibraryTemplateButtonList"
]


# --- restJson1 ser/de ---
def serialize_json(value: MetaLibraryTemplateButtonList) -> list:
    import capo_socialmessaging.types.library_template_button_list

    out: list = []
    for item in value:
        out.append(
            capo_socialmessaging.types.library_template_button_list.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> MetaLibraryTemplateButtonList:
    import capo_socialmessaging.types.library_template_button_list

    out: MetaLibraryTemplateButtonList = []
    for item in data:
        out.append(
            capo_socialmessaging.types.library_template_button_list.deserialize_json(
                item
            )
        )
    return out
