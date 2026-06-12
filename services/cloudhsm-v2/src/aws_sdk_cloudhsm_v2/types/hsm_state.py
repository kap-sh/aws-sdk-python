"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#HsmState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudhsm_v2.errors import DeserializationError

HsmState: TypeAlias = Literal[
    "CREATE_IN_PROGRESS",
    "ACTIVE",
    "DEGRADED",
    "DELETE_IN_PROGRESS",
    "DELETED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATE_IN_PROGRESS",
        "ACTIVE",
        "DEGRADED",
        "DELETE_IN_PROGRESS",
        "DELETED",
    )
)


def serialize_aws_json_1_1(value: HsmState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HsmState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HsmState value: {data!r}")
    return cast(HsmState, data)
