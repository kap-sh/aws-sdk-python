"""Generated from Smithy shape ``com.amazonaws.amp#Source``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_amp.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_amp.types.eks_configuration
    import aws_sdk_amp.types.vpc_configuration


class _Source_eksConfiguration(TypedDict):
    eksConfiguration: "aws_sdk_amp.types.eks_configuration.EksConfiguration"


class _Source_vpcConfiguration(TypedDict):
    vpcConfiguration: "aws_sdk_amp.types.vpc_configuration.VpcConfiguration"


Source: TypeAlias = _Source_eksConfiguration | _Source_vpcConfiguration


# --- restJson1 ser/de ---
def serialize_json(value: Source) -> dict:
    if "eksConfiguration" in value:
        import aws_sdk_amp.types.eks_configuration

        return {
            "eksConfiguration": aws_sdk_amp.types.eks_configuration.serialize_json(
                value["eksConfiguration"]
            )
        }
    elif "vpcConfiguration" in value:
        import aws_sdk_amp.types.vpc_configuration

        return {
            "vpcConfiguration": aws_sdk_amp.types.vpc_configuration.serialize_json(
                value["vpcConfiguration"]
            )
        }
    else:
        raise SerializationError("Source: no variant present")


def deserialize_json(data: dict) -> Source:
    if "eksConfiguration" in data:
        import aws_sdk_amp.types.eks_configuration

        return {
            "eksConfiguration": aws_sdk_amp.types.eks_configuration.deserialize_json(
                data["eksConfiguration"]
            )
        }
    elif "vpcConfiguration" in data:
        import aws_sdk_amp.types.vpc_configuration

        return {
            "vpcConfiguration": aws_sdk_amp.types.vpc_configuration.deserialize_json(
                data["vpcConfiguration"]
            )
        }
    else:
        raise DeserializationError("Source: no recognized variant key")
