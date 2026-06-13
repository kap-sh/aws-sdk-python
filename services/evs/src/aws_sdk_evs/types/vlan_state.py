"""Generated from Smithy shape ``com.amazonaws.evs#VlanState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_evs.errors import DeserializationError

VlanState: TypeAlias = Literal[
    "CREATING",
    "CREATED",
    "DELETING",
    "DELETED",
    "CREATE_FAILED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "CREATED",
        "DELETING",
        "DELETED",
        "CREATE_FAILED",
    )
)


def serialize_aws_json_1_0(value: VlanState) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> VlanState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VlanState value: {data!r}")
    return cast(VlanState, data)
