"""Generated from Smithy shape ``com.amazonaws.quicksight#BodySectionConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.body_section_configuration

BodySectionConfigurationList: TypeAlias = list[
    "aws_sdk_quicksight.types.body_section_configuration.BodySectionConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: BodySectionConfigurationList) -> list:
    import aws_sdk_quicksight.types.body_section_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.body_section_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BodySectionConfigurationList:
    import aws_sdk_quicksight.types.body_section_configuration

    out: BodySectionConfigurationList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.body_section_configuration.deserialize_json(item)
        )
    return out
