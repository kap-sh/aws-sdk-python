"""Generated from Smithy shape ``com.amazonaws.imagebuilder#LifecyclePolicyResourceType``."""

from typing import Literal, TypeAlias, cast

LifecyclePolicyResourceType: TypeAlias = Literal[
    "AMI_IMAGE",
    "CONTAINER_IMAGE",
]


# --- restJson1 ser/de ---
def serialize_json(value: LifecyclePolicyResourceType) -> str:
    return value


def deserialize_json(data: str) -> LifecyclePolicyResourceType:
    return cast(LifecyclePolicyResourceType, data)
