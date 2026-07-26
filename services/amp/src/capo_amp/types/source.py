"""Generated from Smithy shape ``com.amazonaws.amp#Source``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_amp.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_amp.types.eks_configuration
    import capo_amp.types.vpc_configuration


class _Source_eksConfiguration(TypedDict, closed=True):
    eksConfiguration: "capo_amp.types.eks_configuration.EksConfiguration"


class _Source_vpcConfiguration(TypedDict, closed=True):
    vpcConfiguration: "capo_amp.types.vpc_configuration.VpcConfiguration"


Source: TypeAlias = _Source_eksConfiguration | _Source_vpcConfiguration


# --- restJson1 ser/de ---
def serialize_json(value: Source) -> dict:
    if "eksConfiguration" in value:
        import capo_amp.types.eks_configuration

        return {
            "eksConfiguration": capo_amp.types.eks_configuration.serialize_json(
                value["eksConfiguration"]
            )
        }
    elif "vpcConfiguration" in value:
        import capo_amp.types.vpc_configuration

        return {
            "vpcConfiguration": capo_amp.types.vpc_configuration.serialize_json(
                value["vpcConfiguration"]
            )
        }
    else:
        raise SerializationError("Source: no variant present")


def deserialize_json(data: dict) -> Source:
    if "eksConfiguration" in data:
        import capo_amp.types.eks_configuration

        return {
            "eksConfiguration": capo_amp.types.eks_configuration.deserialize_json(
                data["eksConfiguration"]
            )
        }
    elif "vpcConfiguration" in data:
        import capo_amp.types.vpc_configuration

        return {
            "vpcConfiguration": capo_amp.types.vpc_configuration.deserialize_json(
                data["vpcConfiguration"]
            )
        }
    else:
        raise DeserializationError("Source: no recognized variant key")
