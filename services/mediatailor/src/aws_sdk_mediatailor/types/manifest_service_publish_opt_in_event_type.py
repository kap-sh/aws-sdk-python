"""Generated from Smithy shape ``com.amazonaws.mediatailor#ManifestServicePublishOptInEventType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediatailor.errors import DeserializationError

ManifestServicePublishOptInEventType: TypeAlias = Literal[
    "PRE_SESSION_INIT_HOOK_SUMMARY",
    "PRE_SESSION_INIT_FUNCTION_COMPLETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PRE_SESSION_INIT_HOOK_SUMMARY",
        "PRE_SESSION_INIT_FUNCTION_COMPLETED",
    )
)


def serialize_json(value: ManifestServicePublishOptInEventType) -> str:
    return value


def deserialize_json(data: str) -> ManifestServicePublishOptInEventType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ManifestServicePublishOptInEventType value: {data!r}"
        )
    return cast(ManifestServicePublishOptInEventType, data)
