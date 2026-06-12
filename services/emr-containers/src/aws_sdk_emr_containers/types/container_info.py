"""Generated from Smithy shape ``com.amazonaws.emrcontainers#ContainerInfo``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_emr_containers.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_emr_containers.types.eks_info


class _ContainerInfo_eksInfo(TypedDict):
    eksInfo: "aws_sdk_emr_containers.types.eks_info.EksInfo"


ContainerInfo: TypeAlias = _ContainerInfo_eksInfo


# --- restJson1 ser/de ---
def serialize_json(value: ContainerInfo) -> dict:
    if "eksInfo" in value:
        import aws_sdk_emr_containers.types.eks_info

        return {
            "eksInfo": aws_sdk_emr_containers.types.eks_info.serialize_json(
                value["eksInfo"]
            )
        }
    else:
        raise SerializationError("ContainerInfo: no variant present")


def deserialize_json(data: dict) -> ContainerInfo:
    if "eksInfo" in data:
        import aws_sdk_emr_containers.types.eks_info

        return {
            "eksInfo": aws_sdk_emr_containers.types.eks_info.deserialize_json(
                data["eksInfo"]
            )
        }
    else:
        raise DeserializationError("ContainerInfo: no recognized variant key")
