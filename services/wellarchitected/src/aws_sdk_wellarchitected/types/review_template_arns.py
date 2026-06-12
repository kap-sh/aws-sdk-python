"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ReviewTemplateArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.template_arn

ReviewTemplateArns: TypeAlias = list[
    "aws_sdk_wellarchitected.types.template_arn.TemplateArn"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReviewTemplateArns) -> list:
    return list(value)


def deserialize_json(data: list) -> ReviewTemplateArns:
    return list(data)
