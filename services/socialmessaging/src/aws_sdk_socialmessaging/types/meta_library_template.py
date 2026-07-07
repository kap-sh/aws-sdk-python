"""Generated from Smithy shape ``com.amazonaws.socialmessaging#MetaLibraryTemplate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_socialmessaging.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_socialmessaging.types.library_template_body_inputs
    import aws_sdk_socialmessaging.types.meta_library_template_button_inputs
    import aws_sdk_socialmessaging.types.meta_template_category
    import aws_sdk_socialmessaging.types.meta_template_language
    import aws_sdk_socialmessaging.types.meta_template_name


class MetaLibraryTemplate(TypedDict, closed=True):
    template_name: "aws_sdk_socialmessaging.types.meta_template_name.MetaTemplateName"
    """<p>The name to assign to the template.</p>"""
    library_template_name: (
        "aws_sdk_socialmessaging.types.meta_template_name.MetaTemplateName"
    )
    """<p>The name of the template in Meta's library.</p>"""
    template_category: (
        "aws_sdk_socialmessaging.types.meta_template_category.MetaTemplateCategory"
    )
    """<p>The category of the template (for example, UTILITY or MARKETING).</p>"""
    template_language: (
        "aws_sdk_socialmessaging.types.meta_template_language.MetaTemplateLanguage"
    )
    """<p>The language code for the template (for example, en_US).</p>"""
    library_template_button_inputs: NotRequired[
        "aws_sdk_socialmessaging.types.meta_library_template_button_inputs.MetaLibraryTemplateButtonInputs"
    ]
    """<p>Button customizations for the template.</p>"""
    library_template_body_inputs: NotRequired[
        "aws_sdk_socialmessaging.types.library_template_body_inputs.LibraryTemplateBodyInputs"
    ]
    """<p>Body text customizations for the template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetaLibraryTemplate) -> dict:
    out: dict = {}
    out["templateName"] = value["template_name"]
    out["libraryTemplateName"] = value["library_template_name"]
    out["templateCategory"] = value["template_category"]
    out["templateLanguage"] = value["template_language"]
    if "library_template_button_inputs" in value:
        import aws_sdk_socialmessaging.types.meta_library_template_button_inputs

        out["libraryTemplateButtonInputs"] = (
            aws_sdk_socialmessaging.types.meta_library_template_button_inputs.serialize_json(
                value["library_template_button_inputs"]
            )
        )
    if "library_template_body_inputs" in value:
        import aws_sdk_socialmessaging.types.library_template_body_inputs

        out["libraryTemplateBodyInputs"] = (
            aws_sdk_socialmessaging.types.library_template_body_inputs.serialize_json(
                value["library_template_body_inputs"]
            )
        )
    return out


def deserialize_json(data: dict) -> MetaLibraryTemplate:
    out: MetaLibraryTemplate = {}  # type: ignore[typeddict-item]
    if "templateName" in data:
        out["template_name"] = data["templateName"]
    else:
        raise DeserializationError("MetaLibraryTemplate.template_name required")
    if "libraryTemplateName" in data:
        out["library_template_name"] = data["libraryTemplateName"]
    else:
        raise DeserializationError("MetaLibraryTemplate.library_template_name required")
    if "templateCategory" in data:
        out["template_category"] = data["templateCategory"]
    else:
        raise DeserializationError("MetaLibraryTemplate.template_category required")
    if "templateLanguage" in data:
        out["template_language"] = data["templateLanguage"]
    else:
        raise DeserializationError("MetaLibraryTemplate.template_language required")
    if "libraryTemplateButtonInputs" in data:
        import aws_sdk_socialmessaging.types.meta_library_template_button_inputs

        out["library_template_button_inputs"] = (
            aws_sdk_socialmessaging.types.meta_library_template_button_inputs.deserialize_json(
                data["libraryTemplateButtonInputs"]
            )
        )
    if "libraryTemplateBodyInputs" in data:
        import aws_sdk_socialmessaging.types.library_template_body_inputs

        out["library_template_body_inputs"] = (
            aws_sdk_socialmessaging.types.library_template_body_inputs.deserialize_json(
                data["libraryTemplateBodyInputs"]
            )
        )
    return out
