"""Generated from Smithy shape ``com.amazonaws.quicksight#BodySectionRepeatDimensionConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.body_section_repeat_dimension_configuration

BodySectionRepeatDimensionConfigurationList: TypeAlias = list[
    "aws_sdk_quicksight.types.body_section_repeat_dimension_configuration.BodySectionRepeatDimensionConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: BodySectionRepeatDimensionConfigurationList) -> list:
    import aws_sdk_quicksight.types.body_section_repeat_dimension_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.body_section_repeat_dimension_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BodySectionRepeatDimensionConfigurationList:
    import aws_sdk_quicksight.types.body_section_repeat_dimension_configuration

    out: BodySectionRepeatDimensionConfigurationList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.body_section_repeat_dimension_configuration.deserialize_json(
                item
            )
        )
    return out
