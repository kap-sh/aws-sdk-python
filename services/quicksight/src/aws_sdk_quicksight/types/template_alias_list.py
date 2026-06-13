"""Generated from Smithy shape ``com.amazonaws.quicksight#TemplateAliasList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.template_alias

TemplateAliasList: TypeAlias = list[
    "aws_sdk_quicksight.types.template_alias.TemplateAlias"
]


# --- restJson1 ser/de ---
def serialize_json(value: TemplateAliasList) -> list:
    import aws_sdk_quicksight.types.template_alias

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.template_alias.serialize_json(item))
    return out


def deserialize_json(data: list) -> TemplateAliasList:
    import aws_sdk_quicksight.types.template_alias

    out: TemplateAliasList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.template_alias.deserialize_json(item))
    return out
