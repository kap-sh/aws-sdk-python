"""Generated from Smithy shape ``com.amazonaws.socialmessaging#MetaLibraryTemplateButtonList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_socialmessaging.types.library_template_button_list

MetaLibraryTemplateButtonList: TypeAlias = list[
    "aws_sdk_socialmessaging.types.library_template_button_list.LibraryTemplateButtonList"
]


# --- restJson1 ser/de ---
def serialize_json(value: MetaLibraryTemplateButtonList) -> list:
    import aws_sdk_socialmessaging.types.library_template_button_list

    out: list = []
    for item in value:
        out.append(
            aws_sdk_socialmessaging.types.library_template_button_list.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> MetaLibraryTemplateButtonList:
    import aws_sdk_socialmessaging.types.library_template_button_list

    out: MetaLibraryTemplateButtonList = []
    for item in data:
        out.append(
            aws_sdk_socialmessaging.types.library_template_button_list.deserialize_json(
                item
            )
        )
    return out
