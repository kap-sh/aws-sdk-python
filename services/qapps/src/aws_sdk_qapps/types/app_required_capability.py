"""Generated from Smithy shape ``com.amazonaws.qapps#AppRequiredCapability``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qapps.errors import DeserializationError

AppRequiredCapability: TypeAlias = Literal[
    "FileUpload",
    "CreatorMode",
    "RetrievalMode",
    "PluginMode",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FileUpload",
        "CreatorMode",
        "RetrievalMode",
        "PluginMode",
    )
)


def serialize_json(value: AppRequiredCapability) -> str:
    return value


def deserialize_json(data: str) -> AppRequiredCapability:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AppRequiredCapability value: {data!r}")
    return cast(AppRequiredCapability, data)
