"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#DatasetStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lookoutequipment.errors import DeserializationError

DatasetStatus: TypeAlias = Literal[
    "CREATED",
    "INGESTION_IN_PROGRESS",
    "ACTIVE",
    "IMPORT_IN_PROGRESS",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATED",
        "INGESTION_IN_PROGRESS",
        "ACTIVE",
        "IMPORT_IN_PROGRESS",
    )
)


def serialize_aws_json_1_0(value: DatasetStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DatasetStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DatasetStatus value: {data!r}")
    return cast(DatasetStatus, data)
