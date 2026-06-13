"""Generated from Smithy shape ``com.amazonaws.inspector2#DisassociateConfigurationRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.disassociate_configuration_request

DisassociateConfigurationRequestList: TypeAlias = list[
    "aws_sdk_inspector2.types.disassociate_configuration_request.DisassociateConfigurationRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateConfigurationRequestList) -> list:
    import aws_sdk_inspector2.types.disassociate_configuration_request

    out: list = []
    for item in value:
        out.append(
            aws_sdk_inspector2.types.disassociate_configuration_request.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DisassociateConfigurationRequestList:
    import aws_sdk_inspector2.types.disassociate_configuration_request

    out: DisassociateConfigurationRequestList = []
    for item in data:
        out.append(
            aws_sdk_inspector2.types.disassociate_configuration_request.deserialize_json(
                item
            )
        )
    return out
