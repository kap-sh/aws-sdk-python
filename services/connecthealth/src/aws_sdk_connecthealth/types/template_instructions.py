"""Generated from Smithy shape ``com.amazonaws.connecthealth#TemplateInstructions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connecthealth.types.template_section_instruction

TemplateInstructions: TypeAlias = list[
    "aws_sdk_connecthealth.types.template_section_instruction.TemplateSectionInstruction"
]


# --- restJson1 ser/de ---
def serialize_json(value: TemplateInstructions) -> list:
    import aws_sdk_connecthealth.types.template_section_instruction

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connecthealth.types.template_section_instruction.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> TemplateInstructions:
    import aws_sdk_connecthealth.types.template_section_instruction

    out: TemplateInstructions = []
    for item in data:
        out.append(
            aws_sdk_connecthealth.types.template_section_instruction.deserialize_json(
                item
            )
        )
    return out
