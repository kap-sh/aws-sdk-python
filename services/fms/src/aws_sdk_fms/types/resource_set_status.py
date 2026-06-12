"""Generated from Smithy shape ``com.amazonaws.fms#ResourceSetStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fms.errors import DeserializationError

ResourceSetStatus: TypeAlias = Literal[
    "ACTIVE",
    "OUT_OF_ADMIN_SCOPE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "OUT_OF_ADMIN_SCOPE",
    )
)


def serialize_aws_json_1_1(value: ResourceSetStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResourceSetStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceSetStatus value: {data!r}")
    return cast(ResourceSetStatus, data)
