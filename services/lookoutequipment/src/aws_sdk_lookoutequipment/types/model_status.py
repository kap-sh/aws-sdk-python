"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#ModelStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lookoutequipment.errors import DeserializationError

ModelStatus: TypeAlias = Literal[
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


def serialize_aws_json_1_0(value: ModelStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ModelStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ModelStatus value: {data!r}")
    return cast(ModelStatus, data)
