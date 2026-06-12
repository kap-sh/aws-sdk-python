"""Generated from Smithy shape ``com.amazonaws.iotdeviceadvisor#SuiteDefinitionInformationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotdeviceadvisor.types.suite_definition_information

SuiteDefinitionInformationList: TypeAlias = list[
    "aws_sdk_iotdeviceadvisor.types.suite_definition_information.SuiteDefinitionInformation"
]


# --- restJson1 ser/de ---
def serialize_json(value: SuiteDefinitionInformationList) -> list:
    import aws_sdk_iotdeviceadvisor.types.suite_definition_information

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iotdeviceadvisor.types.suite_definition_information.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SuiteDefinitionInformationList:
    import aws_sdk_iotdeviceadvisor.types.suite_definition_information

    out: SuiteDefinitionInformationList = []
    for item in data:
        out.append(
            aws_sdk_iotdeviceadvisor.types.suite_definition_information.deserialize_json(
                item
            )
        )
    return out
