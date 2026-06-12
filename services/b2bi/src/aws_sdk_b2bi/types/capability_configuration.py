"""Generated from Smithy shape ``com.amazonaws.b2bi#CapabilityConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_b2bi.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_b2bi.types.edi_configuration


class _CapabilityConfiguration_edi(TypedDict):
    edi: "aws_sdk_b2bi.types.edi_configuration.EdiConfiguration"


CapabilityConfiguration: TypeAlias = _CapabilityConfiguration_edi


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CapabilityConfiguration) -> dict:
    if "edi" in value:
        import aws_sdk_b2bi.types.edi_configuration

        return {
            "edi": aws_sdk_b2bi.types.edi_configuration.serialize_aws_json_1_0(
                value["edi"]
            )
        }
    else:
        raise SerializationError("CapabilityConfiguration: no variant present")


def deserialize_aws_json_1_0(data: dict) -> CapabilityConfiguration:
    if "edi" in data:
        import aws_sdk_b2bi.types.edi_configuration

        return {
            "edi": aws_sdk_b2bi.types.edi_configuration.deserialize_aws_json_1_0(
                data["edi"]
            )
        }
    else:
        raise DeserializationError("CapabilityConfiguration: no recognized variant key")
