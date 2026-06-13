"""Generated from Smithy shape ``com.amazonaws.quicksight#TemplateErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.template_error

TemplateErrorList: TypeAlias = list[
    "aws_sdk_quicksight.types.template_error.TemplateError"
]


# --- restJson1 ser/de ---
def serialize_json(value: TemplateErrorList) -> list:
    import aws_sdk_quicksight.types.template_error

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.template_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> TemplateErrorList:
    import aws_sdk_quicksight.types.template_error

    out: TemplateErrorList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.template_error.deserialize_json(item))
    return out
