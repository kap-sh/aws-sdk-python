"""Generated from Smithy shape ``com.amazonaws.cloudhsm#HsmStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudhsm.errors import DeserializationError

HsmStatus: TypeAlias = Literal[
    "PENDING",
    "RUNNING",
    "UPDATING",
    "SUSPENDED",
    "TERMINATING",
    "TERMINATED",
    "DEGRADED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "RUNNING",
        "UPDATING",
        "SUSPENDED",
        "TERMINATING",
        "TERMINATED",
        "DEGRADED",
    )
)


def serialize_aws_json_1_1(value: HsmStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HsmStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HsmStatus value: {data!r}")
    return cast(HsmStatus, data)
