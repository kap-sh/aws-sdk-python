"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#IngestionJobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lookoutequipment.errors import DeserializationError

IngestionJobStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "SUCCESS",
    "FAILED",
    "IMPORT_IN_PROGRESS",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "SUCCESS",
        "FAILED",
        "IMPORT_IN_PROGRESS",
    )
)


def serialize_aws_json_1_0(value: IngestionJobStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> IngestionJobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IngestionJobStatus value: {data!r}")
    return cast(IngestionJobStatus, data)
