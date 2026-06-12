"""Generated from Smithy shape ``com.amazonaws.b2bi#Mapping``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_b2bi.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_b2bi.types.mapping_template
    import aws_sdk_b2bi.types.mapping_template_language


class Mapping(TypedDict):
    template_language: (
        "aws_sdk_b2bi.types.mapping_template_language.MappingTemplateLanguage"
    )
    """<p>The transformation language for the template, either XSLT or JSONATA.</p>"""
    template: NotRequired["aws_sdk_b2bi.types.mapping_template.MappingTemplate"]
    """<p>A string that represents the mapping template, in the transformation language specified in <code>templateLanguage</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Mapping) -> dict:
    out: dict = {}
    import aws_sdk_b2bi.types.mapping_template_language

    out["templateLanguage"] = (
        aws_sdk_b2bi.types.mapping_template_language.serialize_aws_json_1_0(
            value["template_language"]
        )
    )
    if "template" in value:
        out["template"] = value["template"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Mapping:
    out: Mapping = {}  # type: ignore[typeddict-item]
    if "templateLanguage" in data:
        import aws_sdk_b2bi.types.mapping_template_language

        out["template_language"] = (
            aws_sdk_b2bi.types.mapping_template_language.deserialize_aws_json_1_0(
                data["templateLanguage"]
            )
        )
    else:
        raise DeserializationError("Mapping.template_language required")
    if "template" in data:
        out["template"] = data["template"]
    return out
