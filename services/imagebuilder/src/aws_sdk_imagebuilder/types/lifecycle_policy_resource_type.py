"""Generated from Smithy shape ``com.amazonaws.imagebuilder#LifecyclePolicyResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_imagebuilder.errors import DeserializationError

LifecyclePolicyResourceType: TypeAlias = Literal[
    "AMI_IMAGE",
    "CONTAINER_IMAGE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AMI_IMAGE",
        "CONTAINER_IMAGE",
    )
)


def serialize_json(value: LifecyclePolicyResourceType) -> str:
    return value


def deserialize_json(data: str) -> LifecyclePolicyResourceType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown LifecyclePolicyResourceType value: {data!r}"
        )
    return cast(LifecyclePolicyResourceType, data)
