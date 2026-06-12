"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#ManifestStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotfleetwise.errors import DeserializationError

ManifestStatus: TypeAlias = Literal[
    "ACTIVE",
    "DRAFT",
    "INVALID",
    "VALIDATING",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "DRAFT",
        "INVALID",
        "VALIDATING",
    )
)


def serialize_aws_json_1_0(value: ManifestStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ManifestStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ManifestStatus value: {data!r}")
    return cast(ManifestStatus, data)
