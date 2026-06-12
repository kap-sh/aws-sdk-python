"""Generated from Smithy shape ``com.amazonaws.opensearch#RolesKeyIdCOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

RolesKeyIdCOption: TypeAlias = Literal[
    "GroupName",
    "GroupId",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GroupName",
        "GroupId",
    )
)


def serialize_json(value: RolesKeyIdCOption) -> str:
    return value


def deserialize_json(data: str) -> RolesKeyIdCOption:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RolesKeyIdCOption value: {data!r}")
    return cast(RolesKeyIdCOption, data)
