"""Generated from Smithy shape ``com.amazonaws.quicksight#HeaderFooterSectionConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.header_footer_section_configuration

HeaderFooterSectionConfigurationList: TypeAlias = list[
    "aws_sdk_quicksight.types.header_footer_section_configuration.HeaderFooterSectionConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: HeaderFooterSectionConfigurationList) -> list:
    import aws_sdk_quicksight.types.header_footer_section_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.header_footer_section_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> HeaderFooterSectionConfigurationList:
    import aws_sdk_quicksight.types.header_footer_section_configuration

    out: HeaderFooterSectionConfigurationList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.header_footer_section_configuration.deserialize_json(
                item
            )
        )
    return out
