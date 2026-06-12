"""Generated from Smithy shape ``com.amazonaws.workdocs#DocumentVersionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workdocs.errors import DeserializationError

DocumentVersionStatus: TypeAlias = Literal["ACTIVE",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ACTIVE",))


def serialize_json(value: DocumentVersionStatus) -> str:
    return value


def deserialize_json(data: str) -> DocumentVersionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DocumentVersionStatus value: {data!r}")
    return cast(DocumentVersionStatus, data)
