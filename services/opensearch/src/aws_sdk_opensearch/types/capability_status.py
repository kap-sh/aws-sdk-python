"""Generated from Smithy shape ``com.amazonaws.opensearch#CapabilityStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

"""<p>The status of a capability. Possible values: <code>creating</code>, <code>create_failed</code>, <code>active</code>, <code>updating</code>, <code>update_failed</code>, <code>deleting</code>, <code>delete_failed</code>.</p>"""
CapabilityStatus: TypeAlias = Literal[
    "creating",
    "create_failed",
    "active",
    "updating",
    "update_failed",
    "deleting",
    "delete_failed",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "creating",
        "create_failed",
        "active",
        "updating",
        "update_failed",
        "deleting",
        "delete_failed",
    )
)


def serialize_json(value: CapabilityStatus) -> str:
    return value


def deserialize_json(data: str) -> CapabilityStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CapabilityStatus value: {data!r}")
    return cast(CapabilityStatus, data)
