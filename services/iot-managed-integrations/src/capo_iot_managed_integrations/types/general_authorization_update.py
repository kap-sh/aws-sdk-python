"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#GeneralAuthorizationUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.auth_materials


class GeneralAuthorizationUpdate(TypedDict, closed=True):
    auth_materials_to_add: NotRequired[
        "capo_iot_managed_integrations.types.auth_materials.AuthMaterials"
    ]
    """<p>The authorization materials to add.</p>"""
    auth_materials_to_update: NotRequired[
        "capo_iot_managed_integrations.types.auth_materials.AuthMaterials"
    ]
    """<p>The authorization materials to update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeneralAuthorizationUpdate) -> dict:
    out: dict = {}
    if "auth_materials_to_add" in value:
        import capo_iot_managed_integrations.types.auth_materials

        out["AuthMaterialsToAdd"] = (
            capo_iot_managed_integrations.types.auth_materials.serialize_json(
                value["auth_materials_to_add"]
            )
        )
    if "auth_materials_to_update" in value:
        import capo_iot_managed_integrations.types.auth_materials

        out["AuthMaterialsToUpdate"] = (
            capo_iot_managed_integrations.types.auth_materials.serialize_json(
                value["auth_materials_to_update"]
            )
        )
    return out


def deserialize_json(data: dict) -> GeneralAuthorizationUpdate:
    out: GeneralAuthorizationUpdate = {}  # type: ignore[typeddict-item]
    if "AuthMaterialsToAdd" in data:
        import capo_iot_managed_integrations.types.auth_materials

        out["auth_materials_to_add"] = (
            capo_iot_managed_integrations.types.auth_materials.deserialize_json(
                data["AuthMaterialsToAdd"]
            )
        )
    if "AuthMaterialsToUpdate" in data:
        import capo_iot_managed_integrations.types.auth_materials

        out["auth_materials_to_update"] = (
            capo_iot_managed_integrations.types.auth_materials.deserialize_json(
                data["AuthMaterialsToUpdate"]
            )
        )
    return out
