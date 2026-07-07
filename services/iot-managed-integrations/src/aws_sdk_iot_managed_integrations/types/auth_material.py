"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#AuthMaterial``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iot_managed_integrations.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.auth_material_name
    import aws_sdk_iot_managed_integrations.types.secrets_manager


class AuthMaterial(TypedDict, closed=True):
    secrets_manager: (
        "aws_sdk_iot_managed_integrations.types.secrets_manager.SecretsManager"
    )
    auth_material_name: (
        "aws_sdk_iot_managed_integrations.types.auth_material_name.AuthMaterialName"
    )
    """<p>The name of the authorization material.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuthMaterial) -> dict:
    out: dict = {}
    import aws_sdk_iot_managed_integrations.types.secrets_manager

    out["SecretsManager"] = (
        aws_sdk_iot_managed_integrations.types.secrets_manager.serialize_json(
            value["secrets_manager"]
        )
    )
    out["AuthMaterialName"] = value["auth_material_name"]
    return out


def deserialize_json(data: dict) -> AuthMaterial:
    out: AuthMaterial = {}  # type: ignore[typeddict-item]
    if "SecretsManager" in data:
        import aws_sdk_iot_managed_integrations.types.secrets_manager

        out["secrets_manager"] = (
            aws_sdk_iot_managed_integrations.types.secrets_manager.deserialize_json(
                data["SecretsManager"]
            )
        )
    else:
        raise DeserializationError("AuthMaterial.secrets_manager required")
    if "AuthMaterialName" in data:
        out["auth_material_name"] = data["AuthMaterialName"]
    else:
        raise DeserializationError("AuthMaterial.auth_material_name required")
    return out
