"""Generated from Smithy shape ``com.amazonaws.supplychain#ConfigurationJobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_supplychain.errors import DeserializationError

"""<p>The status of the job.</p>"""
ConfigurationJobStatus: TypeAlias = Literal[
    "NEW",
    "FAILED",
    "IN_PROGRESS",
    "QUEUED",
    "SUCCESS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NEW",
        "FAILED",
        "IN_PROGRESS",
        "QUEUED",
        "SUCCESS",
    )
)


def serialize_json(value: ConfigurationJobStatus) -> str:
    return value


def deserialize_json(data: str) -> ConfigurationJobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConfigurationJobStatus value: {data!r}")
    return cast(ConfigurationJobStatus, data)
