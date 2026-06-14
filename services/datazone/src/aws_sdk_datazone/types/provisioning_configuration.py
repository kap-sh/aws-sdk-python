"""Generated from Smithy shape ``com.amazonaws.datazone#ProvisioningConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.lake_formation_configuration


class _ProvisioningConfiguration_lakeFormationConfiguration(TypedDict):
    lakeFormationConfiguration: (
        "aws_sdk_datazone.types.lake_formation_configuration.LakeFormationConfiguration"
    )


ProvisioningConfiguration: TypeAlias = (
    _ProvisioningConfiguration_lakeFormationConfiguration
)


# --- restJson1 ser/de ---
def serialize_json(value: ProvisioningConfiguration) -> dict:
    if "lakeFormationConfiguration" in value:
        import aws_sdk_datazone.types.lake_formation_configuration

        return {
            "lakeFormationConfiguration": aws_sdk_datazone.types.lake_formation_configuration.serialize_json(
                value["lakeFormationConfiguration"]
            )
        }
    else:
        raise SerializationError("ProvisioningConfiguration: no variant present")


def deserialize_json(data: dict) -> ProvisioningConfiguration:
    if "lakeFormationConfiguration" in data:
        import aws_sdk_datazone.types.lake_formation_configuration

        return {
            "lakeFormationConfiguration": aws_sdk_datazone.types.lake_formation_configuration.deserialize_json(
                data["lakeFormationConfiguration"]
            )
        }
    else:
        raise DeserializationError(
            "ProvisioningConfiguration: no recognized variant key"
        )
