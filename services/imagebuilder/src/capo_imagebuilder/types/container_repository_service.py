"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ContainerRepositoryService``."""

from typing import Literal, TypeAlias, cast

ContainerRepositoryService: TypeAlias = Literal["ECR",]


# --- restJson1 ser/de ---
def serialize_json(value: ContainerRepositoryService) -> str:
    return value


def deserialize_json(data: str) -> ContainerRepositoryService:
    return cast(ContainerRepositoryService, data)
