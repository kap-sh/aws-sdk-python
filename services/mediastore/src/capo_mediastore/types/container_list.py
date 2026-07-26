"""Generated from Smithy shape ``com.amazonaws.mediastore#ContainerList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediastore.types.container

ContainerList: TypeAlias = list["capo_mediastore.types.container.Container"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerList) -> list:
    import capo_mediastore.types.container

    out: list = []
    for item in value:
        out.append(capo_mediastore.types.container.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ContainerList:
    import capo_mediastore.types.container

    out: ContainerList = []
    for item in data:
        out.append(capo_mediastore.types.container.deserialize_aws_json_1_1(item))
    return out
