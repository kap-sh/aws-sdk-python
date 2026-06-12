"""Generated from Smithy shape ``com.amazonaws.efs#TransitionToPrimaryStorageClassRules``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_efs.errors import DeserializationError

TransitionToPrimaryStorageClassRules: TypeAlias = Literal["AFTER_1_ACCESS",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("AFTER_1_ACCESS",))


def serialize_json(value: TransitionToPrimaryStorageClassRules) -> str:
    return value


def deserialize_json(data: str) -> TransitionToPrimaryStorageClassRules:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown TransitionToPrimaryStorageClassRules value: {data!r}"
        )
    return cast(TransitionToPrimaryStorageClassRules, data)
