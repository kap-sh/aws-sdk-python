"""Generated from Smithy shape ``com.amazonaws.elementalinference#DictionaryStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elementalinference.errors import DeserializationError

DictionaryStatus: TypeAlias = Literal[
    "CREATING",
    "AVAILABLE",
    "REFERENCED",
    "DELETING",
    "DELETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "AVAILABLE",
        "REFERENCED",
        "DELETING",
        "DELETED",
    )
)


def serialize_json(value: DictionaryStatus) -> str:
    return value


def deserialize_json(data: str) -> DictionaryStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DictionaryStatus value: {data!r}")
    return cast(DictionaryStatus, data)
