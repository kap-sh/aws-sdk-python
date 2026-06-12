"""Generated from Smithy shape ``com.amazonaws.servicecatalog#CopyProductStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_service_catalog.errors import DeserializationError

CopyProductStatus: TypeAlias = Literal[
    "SUCCEEDED",
    "IN_PROGRESS",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUCCEEDED",
        "IN_PROGRESS",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: CopyProductStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CopyProductStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CopyProductStatus value: {data!r}")
    return cast(CopyProductStatus, data)
