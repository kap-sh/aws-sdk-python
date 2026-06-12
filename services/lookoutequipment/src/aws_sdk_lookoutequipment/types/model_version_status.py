"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#ModelVersionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lookoutequipment.errors import DeserializationError

ModelVersionStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "SUCCESS",
    "FAILED",
    "IMPORT_IN_PROGRESS",
    "CANCELED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "SUCCESS",
        "FAILED",
        "IMPORT_IN_PROGRESS",
        "CANCELED",
    )
)


def serialize_aws_json_1_0(value: ModelVersionStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ModelVersionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ModelVersionStatus value: {data!r}")
    return cast(ModelVersionStatus, data)
