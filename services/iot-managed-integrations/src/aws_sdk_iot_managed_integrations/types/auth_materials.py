"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#AuthMaterials``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.auth_material

AuthMaterials: TypeAlias = list[
    "aws_sdk_iot_managed_integrations.types.auth_material.AuthMaterial"
]


# --- restJson1 ser/de ---
def serialize_json(value: AuthMaterials) -> list:
    import aws_sdk_iot_managed_integrations.types.auth_material

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iot_managed_integrations.types.auth_material.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AuthMaterials:
    import aws_sdk_iot_managed_integrations.types.auth_material

    out: AuthMaterials = []
    for item in data:
        out.append(
            aws_sdk_iot_managed_integrations.types.auth_material.deserialize_json(item)
        )
    return out
