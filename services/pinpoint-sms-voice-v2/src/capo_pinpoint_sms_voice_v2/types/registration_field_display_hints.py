"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#RegistrationFieldDisplayHints``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.select_option_descriptions_list


class RegistrationFieldDisplayHints(TypedDict, closed=True):
    title: "str"
    """<p>The title of the display hint.</p>"""
    short_description: "str"
    """<p>A short description of the display hint.</p>"""
    long_description: NotRequired["str"]
    """<p>A full description of the display hint.</p>"""
    documentation_title: NotRequired["str"]
    """<p>The title of the document the display hint is associated with.</p>"""
    documentation_link: NotRequired["str"]
    """<p>The link to the document the display hint is associated with.</p>"""
    select_option_descriptions: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.select_option_descriptions_list.SelectOptionDescriptionsList"
    ]
    """<p>An array of SelectOptionDescription objects.</p>"""
    text_validation_description: NotRequired["str"]
    """<p>The validation rules for the text field.</p>"""
    example_text_value: NotRequired["str"]
    """<p>Example text of what the value of a field should contain.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RegistrationFieldDisplayHints) -> dict:
    out: dict = {}
    out["Title"] = value["title"]
    out["ShortDescription"] = value["short_description"]
    if "long_description" in value:
        out["LongDescription"] = value["long_description"]
    if "documentation_title" in value:
        out["DocumentationTitle"] = value["documentation_title"]
    if "documentation_link" in value:
        out["DocumentationLink"] = value["documentation_link"]
    if "select_option_descriptions" in value:
        import capo_pinpoint_sms_voice_v2.types.select_option_descriptions_list

        out["SelectOptionDescriptions"] = (
            capo_pinpoint_sms_voice_v2.types.select_option_descriptions_list.serialize_aws_json_1_0(
                value["select_option_descriptions"]
            )
        )
    if "text_validation_description" in value:
        out["TextValidationDescription"] = value["text_validation_description"]
    if "example_text_value" in value:
        out["ExampleTextValue"] = value["example_text_value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RegistrationFieldDisplayHints:
    out: RegistrationFieldDisplayHints = {}  # type: ignore[typeddict-item]
    if "Title" in data:
        out["title"] = data["Title"]
    else:
        raise DeserializationError("RegistrationFieldDisplayHints.title required")
    if "ShortDescription" in data:
        out["short_description"] = data["ShortDescription"]
    else:
        raise DeserializationError(
            "RegistrationFieldDisplayHints.short_description required"
        )
    if "LongDescription" in data:
        out["long_description"] = data["LongDescription"]
    if "DocumentationTitle" in data:
        out["documentation_title"] = data["DocumentationTitle"]
    if "DocumentationLink" in data:
        out["documentation_link"] = data["DocumentationLink"]
    if "SelectOptionDescriptions" in data:
        import capo_pinpoint_sms_voice_v2.types.select_option_descriptions_list

        out["select_option_descriptions"] = (
            capo_pinpoint_sms_voice_v2.types.select_option_descriptions_list.deserialize_aws_json_1_0(
                data["SelectOptionDescriptions"]
            )
        )
    if "TextValidationDescription" in data:
        out["text_validation_description"] = data["TextValidationDescription"]
    if "ExampleTextValue" in data:
        out["example_text_value"] = data["ExampleTextValue"]
    return out
