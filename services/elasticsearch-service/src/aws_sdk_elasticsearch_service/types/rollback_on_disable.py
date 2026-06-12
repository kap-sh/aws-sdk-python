"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#RollbackOnDisable``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elasticsearch_service.errors import DeserializationError

"""<p>Specifies the rollback state while disabling Auto-Tune for the domain. Valid values are NO_ROLLBACK, DEFAULT_ROLLBACK.</p>"""
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
