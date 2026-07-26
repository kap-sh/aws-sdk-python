"""Generated from Smithy shape ``com.amazonaws.devicefarm#Artifacts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_device_farm.types.artifact

Artifacts: TypeAlias = list["capo_device_farm.types.artifact.Artifact"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Artifacts) -> list:
    import capo_device_farm.types.artifact

    out: list = []
    for item in value:
        out.append(capo_device_farm.types.artifact.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Artifacts:
    import capo_device_farm.types.artifact

    out: Artifacts = []
    for item in data:
        out.append(capo_device_farm.types.artifact.deserialize_aws_json_1_1(item))
    return out
