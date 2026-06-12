"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ContainerRepositoryService``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_imagebuilder.errors import DeserializationError

ContainerRepositoryService: TypeAlias = Literal["ECR",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ECR",))


def serialize_json(value: ContainerRepositoryService) -> str:
    return value


def deserialize_json(data: str) -> ContainerRepositoryService:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ContainerRepositoryService value: {data!r}"
        )
    return cast(ContainerRepositoryService, data)
