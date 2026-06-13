"""Generated from Smithy shape ``com.amazonaws.pcaconnectorscep#MobileDeviceManagement``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_pca_connector_scep.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_pca_connector_scep.types.intune_configuration


class _MobileDeviceManagement_Intune(TypedDict):
    Intune: "aws_sdk_pca_connector_scep.types.intune_configuration.IntuneConfiguration"


MobileDeviceManagement: TypeAlias = _MobileDeviceManagement_Intune


# --- restJson1 ser/de ---
def serialize_json(value: MobileDeviceManagement) -> dict:
    if "Intune" in value:
        import aws_sdk_pca_connector_scep.types.intune_configuration

        return {
            "Intune": aws_sdk_pca_connector_scep.types.intune_configuration.serialize_json(
                value["Intune"]
            )
        }
    else:
        raise SerializationError("MobileDeviceManagement: no variant present")


def deserialize_json(data: dict) -> MobileDeviceManagement:
    if "Intune" in data:
        import aws_sdk_pca_connector_scep.types.intune_configuration

        return {
            "Intune": aws_sdk_pca_connector_scep.types.intune_configuration.deserialize_json(
                data["Intune"]
            )
        }
    else:
        raise DeserializationError("MobileDeviceManagement: no recognized variant key")
