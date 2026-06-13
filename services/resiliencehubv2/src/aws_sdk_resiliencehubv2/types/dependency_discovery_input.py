"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#DependencyDiscoveryInput``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehubv2.errors import DeserializationError

"""<p>Caller-settable values for dependency discovery. INITIALIZING is system-managed.</p>"""
DependencyDiscoveryInput: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: DependencyDiscoveryInput) -> str:
    return value


def deserialize_json(data: str) -> DependencyDiscoveryInput:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DependencyDiscoveryInput value: {data!r}")
    return cast(DependencyDiscoveryInput, data)
