"""Generated from Smithy shape ``com.amazonaws.opensearch#RolesKeyIdCOption``."""

from typing import Literal, TypeAlias, cast

RolesKeyIdCOption: TypeAlias = Literal[
    "GroupName",
    "GroupId",
]


# --- restJson1 ser/de ---
def serialize_json(value: RolesKeyIdCOption) -> str:
    return value


def deserialize_json(data: str) -> RolesKeyIdCOption:
    return cast(RolesKeyIdCOption, data)
