"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ContainerType``."""

from typing import Literal, TypeAlias, cast

ContainerType: TypeAlias = Literal["DOCKER",]


# --- restJson1 ser/de ---
def serialize_json(value: ContainerType) -> str:
    return value


def deserialize_json(data: str) -> ContainerType:
    return cast(ContainerType, data)
