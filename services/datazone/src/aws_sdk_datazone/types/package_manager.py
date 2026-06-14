"""Generated from Smithy shape ``com.amazonaws.datazone#PackageManager``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

"""<p>The package manager for a notebook run environment in Amazon SageMaker Unified Studio.</p>"""
PackageManager: TypeAlias = Literal["UV",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("UV",))


def serialize_json(value: PackageManager) -> str:
    return value


def deserialize_json(data: str) -> PackageManager:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PackageManager value: {data!r}")
    return cast(PackageManager, data)
