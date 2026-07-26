"""Generated from Smithy shape ``com.amazonaws.emrcontainers#ContainerProviderType``."""

from typing import Literal, TypeAlias, cast

ContainerProviderType: TypeAlias = Literal["EKS",]


# --- restJson1 ser/de ---
def serialize_json(value: ContainerProviderType) -> str:
    return value


def deserialize_json(data: str) -> ContainerProviderType:
    return cast(ContainerProviderType, data)
