"""Generated from Smithy shape ``com.amazonaws.opensearch#RollbackOnDisable``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

"""<p>The rollback state while disabling Auto-Tune for the domain.</p>"""
RollbackOnDisable: TypeAlias = Literal[
    "NO_ROLLBACK",
    "DEFAULT_ROLLBACK",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NO_ROLLBACK",
        "DEFAULT_ROLLBACK",
    )
)


def serialize_json(value: RollbackOnDisable) -> str:
    return value


def deserialize_json(data: str) -> RollbackOnDisable:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RollbackOnDisable value: {data!r}")
    return cast(RollbackOnDisable, data)
