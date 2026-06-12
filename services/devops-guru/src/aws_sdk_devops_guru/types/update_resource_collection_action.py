"""Generated from Smithy shape ``com.amazonaws.devopsguru#UpdateResourceCollectionAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_devops_guru.errors import DeserializationError

UpdateResourceCollectionAction: TypeAlias = Literal[
    "ADD",
    "REMOVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ADD",
        "REMOVE",
    )
)


def serialize_json(value: UpdateResourceCollectionAction) -> str:
    return value


def deserialize_json(data: str) -> UpdateResourceCollectionAction:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown UpdateResourceCollectionAction value: {data!r}"
        )
    return cast(UpdateResourceCollectionAction, data)
