"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ProvisioningProfileListDefinition``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.provisioning_profile_summary

ProvisioningProfileListDefinition: TypeAlias = list[
    "capo_iot_managed_integrations.types.provisioning_profile_summary.ProvisioningProfileSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProvisioningProfileListDefinition) -> list:
    import capo_iot_managed_integrations.types.provisioning_profile_summary

    out: list = []
    for item in value:
        out.append(
            capo_iot_managed_integrations.types.provisioning_profile_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ProvisioningProfileListDefinition:
    import capo_iot_managed_integrations.types.provisioning_profile_summary

    out: ProvisioningProfileListDefinition = []
    for item in data:
        out.append(
            capo_iot_managed_integrations.types.provisioning_profile_summary.deserialize_json(
                item
            )
        )
    return out
