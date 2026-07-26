"""Generated from Smithy shape ``com.amazonaws.datazone#ProvisioningConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.provisioning_configuration

ProvisioningConfigurationList: TypeAlias = list[
    "capo_datazone.types.provisioning_configuration.ProvisioningConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProvisioningConfigurationList) -> list:
    import capo_datazone.types.provisioning_configuration

    out: list = []
    for item in value:
        out.append(capo_datazone.types.provisioning_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> ProvisioningConfigurationList:
    import capo_datazone.types.provisioning_configuration

    out: ProvisioningConfigurationList = []
    for item in data:
        out.append(
            capo_datazone.types.provisioning_configuration.deserialize_json(item)
        )
    return out
