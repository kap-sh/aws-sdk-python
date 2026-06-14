"""Generated from Smithy shape ``com.amazonaws.datazone#ProvisioningProperties``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.cloud_formation_properties


class _ProvisioningProperties_cloudFormation(TypedDict):
    cloudFormation: (
        "aws_sdk_datazone.types.cloud_formation_properties.CloudFormationProperties"
    )


ProvisioningProperties: TypeAlias = _ProvisioningProperties_cloudFormation


# --- restJson1 ser/de ---
def serialize_json(value: ProvisioningProperties) -> dict:
    if "cloudFormation" in value:
        import aws_sdk_datazone.types.cloud_formation_properties

        return {
            "cloudFormation": aws_sdk_datazone.types.cloud_formation_properties.serialize_json(
                value["cloudFormation"]
            )
        }
    else:
        raise SerializationError("ProvisioningProperties: no variant present")


def deserialize_json(data: dict) -> ProvisioningProperties:
    if "cloudFormation" in data:
        import aws_sdk_datazone.types.cloud_formation_properties

        return {
            "cloudFormation": aws_sdk_datazone.types.cloud_formation_properties.deserialize_json(
                data["cloudFormation"]
            )
        }
    else:
        raise DeserializationError("ProvisioningProperties: no recognized variant key")
