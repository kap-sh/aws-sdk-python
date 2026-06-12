"""Generated from Smithy shape ``com.amazonaws.ssoadmin#RegionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sso_admin.errors import DeserializationError

RegionStatus: TypeAlias = Literal[
    "ACTIVE",
    "ADDING",
    "REMOVING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "ADDING",
        "REMOVING",
    )
)


def serialize_aws_json_1_1(value: RegionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RegionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RegionStatus value: {data!r}")
    return cast(RegionStatus, data)
