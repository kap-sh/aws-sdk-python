"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#TemplateInputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_migrationhuborchestrator.types.template_input

TemplateInputList: TypeAlias = list[
    "aws_sdk_migrationhuborchestrator.types.template_input.TemplateInput"
]


# --- restJson1 ser/de ---
def serialize_json(value: TemplateInputList) -> list:
    import aws_sdk_migrationhuborchestrator.types.template_input

    out: list = []
    for item in value:
        out.append(
            aws_sdk_migrationhuborchestrator.types.template_input.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TemplateInputList:
    import aws_sdk_migrationhuborchestrator.types.template_input

    out: TemplateInputList = []
    for item in data:
        out.append(
            aws_sdk_migrationhuborchestrator.types.template_input.deserialize_json(item)
        )
    return out
