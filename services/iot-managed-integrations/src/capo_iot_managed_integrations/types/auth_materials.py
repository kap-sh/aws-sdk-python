"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#AuthMaterials``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.auth_material

AuthMaterials: TypeAlias = list[
    "capo_iot_managed_integrations.types.auth_material.AuthMaterial"
]


# --- restJson1 ser/de ---
def serialize_json(value: AuthMaterials) -> list:
    import capo_iot_managed_integrations.types.auth_material

    out: list = []
    for item in value:
        out.append(
            capo_iot_managed_integrations.types.auth_material.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AuthMaterials:
    import capo_iot_managed_integrations.types.auth_material

    out: AuthMaterials = []
    for item in data:
        out.append(
            capo_iot_managed_integrations.types.auth_material.deserialize_json(item)
        )
    return out
