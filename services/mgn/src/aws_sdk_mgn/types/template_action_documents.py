"""Generated from Smithy shape ``com.amazonaws.mgn#TemplateActionDocuments``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mgn.types.template_action_document

TemplateActionDocuments: TypeAlias = list[
    "aws_sdk_mgn.types.template_action_document.TemplateActionDocument"
]


# --- restJson1 ser/de ---
def serialize_json(value: TemplateActionDocuments) -> list:
    import aws_sdk_mgn.types.template_action_document

    out: list = []
    for item in value:
        out.append(aws_sdk_mgn.types.template_action_document.serialize_json(item))
    return out


def deserialize_json(data: list) -> TemplateActionDocuments:
    import aws_sdk_mgn.types.template_action_document

    out: TemplateActionDocuments = []
    for item in data:
        out.append(aws_sdk_mgn.types.template_action_document.deserialize_json(item))
    return out
