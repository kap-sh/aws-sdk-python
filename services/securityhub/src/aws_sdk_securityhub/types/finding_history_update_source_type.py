"""Generated from Smithy shape ``com.amazonaws.securityhub#FindingHistoryUpdateSourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

FindingHistoryUpdateSourceType: TypeAlias = Literal[
    "BATCH_UPDATE_FINDINGS",
    "BATCH_IMPORT_FINDINGS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BATCH_UPDATE_FINDINGS",
        "BATCH_IMPORT_FINDINGS",
    )
)


def serialize_json(value: FindingHistoryUpdateSourceType) -> str:
    return value


def deserialize_json(data: str) -> FindingHistoryUpdateSourceType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown FindingHistoryUpdateSourceType value: {data!r}"
        )
    return cast(FindingHistoryUpdateSourceType, data)
