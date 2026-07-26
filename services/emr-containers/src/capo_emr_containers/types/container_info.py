"""Generated from Smithy shape ``com.amazonaws.emrcontainers#ContainerInfo``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_emr_containers.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_emr_containers.types.eks_info


class _ContainerInfo_eksInfo(TypedDict, closed=True):
    eksInfo: "capo_emr_containers.types.eks_info.EksInfo"


ContainerInfo: TypeAlias = _ContainerInfo_eksInfo


# --- restJson1 ser/de ---
def serialize_json(value: ContainerInfo) -> dict:
    if "eksInfo" in value:
        import capo_emr_containers.types.eks_info

        return {
            "eksInfo": capo_emr_containers.types.eks_info.serialize_json(
                value["eksInfo"]
            )
        }
    else:
        raise SerializationError("ContainerInfo: no variant present")


def deserialize_json(data: dict) -> ContainerInfo:
    if "eksInfo" in data:
        import capo_emr_containers.types.eks_info

        return {
            "eksInfo": capo_emr_containers.types.eks_info.deserialize_json(
                data["eksInfo"]
            )
        }
    else:
        raise DeserializationError("ContainerInfo: no recognized variant key")
