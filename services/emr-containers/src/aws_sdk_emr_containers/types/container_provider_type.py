"""Generated from Smithy shape ``com.amazonaws.emrcontainers#ContainerProviderType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_emr_containers.errors import DeserializationError

ContainerProviderType: TypeAlias = Literal["EKS",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("EKS",))


def serialize_json(value: ContainerProviderType) -> str:
    return value


def deserialize_json(data: str) -> ContainerProviderType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContainerProviderType value: {data!r}")
    return cast(ContainerProviderType, data)
