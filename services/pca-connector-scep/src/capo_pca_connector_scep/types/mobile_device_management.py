"""Generated from Smithy shape ``com.amazonaws.pcaconnectorscep#MobileDeviceManagement``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_pca_connector_scep.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_pca_connector_scep.types.intune_configuration


class _MobileDeviceManagement_Intune(TypedDict, closed=True):
    Intune: "capo_pca_connector_scep.types.intune_configuration.IntuneConfiguration"


MobileDeviceManagement: TypeAlias = _MobileDeviceManagement_Intune


# --- restJson1 ser/de ---
def serialize_json(value: MobileDeviceManagement) -> dict:
    if "Intune" in value:
        import capo_pca_connector_scep.types.intune_configuration

        return {
            "Intune": capo_pca_connector_scep.types.intune_configuration.serialize_json(
                value["Intune"]
            )
        }
    else:
        raise SerializationError("MobileDeviceManagement: no variant present")


def deserialize_json(data: dict) -> MobileDeviceManagement:
    if "Intune" in data:
        import capo_pca_connector_scep.types.intune_configuration

        return {
            "Intune": capo_pca_connector_scep.types.intune_configuration.deserialize_json(
                data["Intune"]
            )
        }
    else:
        raise DeserializationError("MobileDeviceManagement: no recognized variant key")
