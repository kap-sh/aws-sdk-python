"""Generated from Smithy shape ``com.amazonaws.socialmessaging#MetaLibraryTemplateDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_socialmessaging.types.meta_industries
    import capo_socialmessaging.types.meta_library_template_button_list
    import capo_socialmessaging.types.meta_template_body
    import capo_socialmessaging.types.meta_template_body_example_params
    import capo_socialmessaging.types.meta_template_category
    import capo_socialmessaging.types.meta_template_header
    import capo_socialmessaging.types.meta_template_id
    import capo_socialmessaging.types.meta_template_language
    import capo_socialmessaging.types.meta_template_name
    import capo_socialmessaging.types.meta_template_topic
    import capo_socialmessaging.types.meta_template_use_case


class MetaLibraryTemplateDefinition(TypedDict, closed=True):
    template_name: NotRequired[
        "capo_socialmessaging.types.meta_template_name.MetaTemplateName"
    ]
    """<p>The name of the template.</p>"""
    template_language: NotRequired[
        "capo_socialmessaging.types.meta_template_language.MetaTemplateLanguage"
    ]
    """<p>The language code for the template (for example, en_US).</p>"""
    template_category: NotRequired[
        "capo_socialmessaging.types.meta_template_category.MetaTemplateCategory"
    ]
    """<p>The category of the template (for example, UTILITY or MARKETING).</p>"""
    template_topic: NotRequired[
        "capo_socialmessaging.types.meta_template_topic.MetaTemplateTopic"
    ]
    """<p>The topic or subject matter of the template.</p>"""
    template_use_case: NotRequired[
        "capo_socialmessaging.types.meta_template_use_case.MetaTemplateUseCase"
    ]
    """<p>The intended use case for the template.</p>"""
    template_industry: NotRequired[
        "capo_socialmessaging.types.meta_industries.MetaIndustries"
    ]
    """<p>The industries the template is designed for.</p>"""
    template_header: NotRequired[
        "capo_socialmessaging.types.meta_template_header.MetaTemplateHeader"
    ]
    """<p>The header text of the template.</p>"""
    template_body: NotRequired[
        "capo_socialmessaging.types.meta_template_body.MetaTemplateBody"
    ]
    """<p>The body text of the template.</p>"""
    template_buttons: NotRequired[
        "capo_socialmessaging.types.meta_library_template_button_list.MetaLibraryTemplateButtonList"
    ]
    """<p>The buttons included in the template.</p>"""
    template_id: NotRequired[
        "capo_socialmessaging.types.meta_template_id.MetaTemplateId"
    ]
    """<p>The ID of the template in Meta's library.</p>"""
    template_body_example_params: NotRequired[
        "capo_socialmessaging.types.meta_template_body_example_params.MetaTemplateBodyExampleParams"
    ]
    """<p>Example parameter values for the template body, used to demonstrate how dynamic content appears in the template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetaLibraryTemplateDefinition) -> dict:
    out: dict = {}
    if "template_name" in value:
        out["templateName"] = value["template_name"]
    if "template_language" in value:
        out["templateLanguage"] = value["template_language"]
    if "template_category" in value:
        out["templateCategory"] = value["template_category"]
    if "template_topic" in value:
        out["templateTopic"] = value["template_topic"]
    if "template_use_case" in value:
        out["templateUseCase"] = value["template_use_case"]
    if "template_industry" in value:
        import capo_socialmessaging.types.meta_industries

        out["templateIndustry"] = (
            capo_socialmessaging.types.meta_industries.serialize_json(
                value["template_industry"]
            )
        )
    if "template_header" in value:
        out["templateHeader"] = value["template_header"]
    if "template_body" in value:
        out["templateBody"] = value["template_body"]
    if "template_buttons" in value:
        import capo_socialmessaging.types.meta_library_template_button_list

        out["templateButtons"] = (
            capo_socialmessaging.types.meta_library_template_button_list.serialize_json(
                value["template_buttons"]
            )
        )
    if "template_id" in value:
        out["templateId"] = value["template_id"]
    if "template_body_example_params" in value:
        import capo_socialmessaging.types.meta_template_body_example_params

        out["templateBodyExampleParams"] = (
            capo_socialmessaging.types.meta_template_body_example_params.serialize_json(
                value["template_body_example_params"]
            )
        )
    return out


def deserialize_json(data: dict) -> MetaLibraryTemplateDefinition:
    out: MetaLibraryTemplateDefinition = {}  # type: ignore[typeddict-item]
    if "templateName" in data:
        out["template_name"] = data["templateName"]
    if "templateLanguage" in data:
        out["template_language"] = data["templateLanguage"]
    if "templateCategory" in data:
        out["template_category"] = data["templateCategory"]
    if "templateTopic" in data:
        out["template_topic"] = data["templateTopic"]
    if "templateUseCase" in data:
        out["template_use_case"] = data["templateUseCase"]
    if "templateIndustry" in data:
        import capo_socialmessaging.types.meta_industries

        out["template_industry"] = (
            capo_socialmessaging.types.meta_industries.deserialize_json(
                data["templateIndustry"]
            )
        )
    if "templateHeader" in data:
        out["template_header"] = data["templateHeader"]
    if "templateBody" in data:
        out["template_body"] = data["templateBody"]
    if "templateButtons" in data:
        import capo_socialmessaging.types.meta_library_template_button_list

        out["template_buttons"] = (
            capo_socialmessaging.types.meta_library_template_button_list.deserialize_json(
                data["templateButtons"]
            )
        )
    if "templateId" in data:
        out["template_id"] = data["templateId"]
    if "templateBodyExampleParams" in data:
        import capo_socialmessaging.types.meta_template_body_example_params

        out["template_body_example_params"] = (
            capo_socialmessaging.types.meta_template_body_example_params.deserialize_json(
                data["templateBodyExampleParams"]
            )
        )
    return out
