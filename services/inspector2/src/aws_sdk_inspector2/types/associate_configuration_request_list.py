"""Generated from Smithy shape ``com.amazonaws.inspector2#AssociateConfigurationRequestList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_inspector2.types.associate_configuration_request

AssociateConfigurationRequestList: TypeAlias = list["aws_sdk_inspector2.types.associate_configuration_request.AssociateConfigurationRequest"]


# --- restJson1 ser/de ---
def serialize_json(value: AssociateConfigurationRequestList) -> list:
    import aws_sdk_inspector2.types.associate_configuration_request
    out: list = []
    for item in value:
        out.append(aws_sdk_inspector2.types.associate_configuration_request.serialize_json(item))
    return out


def deserialize_json(data: list) -> AssociateConfigurationRequestList:
    import aws_sdk_inspector2.types.associate_configuration_request
    out: AssociateConfigurationRequestList = []
    for item in data:
        out.append(aws_sdk_inspector2.types.associate_configuration_request.deserialize_json(item))
    return out