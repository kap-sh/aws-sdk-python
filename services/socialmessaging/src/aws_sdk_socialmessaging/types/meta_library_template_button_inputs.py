"""Generated from Smithy shape ``com.amazonaws.socialmessaging#MetaLibraryTemplateButtonInputs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_socialmessaging.types.library_template_button_input

MetaLibraryTemplateButtonInputs: TypeAlias = list[
    "aws_sdk_socialmessaging.types.library_template_button_input.LibraryTemplateButtonInput"
]


# --- restJson1 ser/de ---
def serialize_json(value: MetaLibraryTemplateButtonInputs) -> list:
    import aws_sdk_socialmessaging.types.library_template_button_input

    out: list = []
    for item in value:
        out.append(
            aws_sdk_socialmessaging.types.library_template_button_input.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> MetaLibraryTemplateButtonInputs:
    import aws_sdk_socialmessaging.types.library_template_button_input

    out: MetaLibraryTemplateButtonInputs = []
    for item in data:
        out.append(
            aws_sdk_socialmessaging.types.library_template_button_input.deserialize_json(
                item
            )
        )
    return out
