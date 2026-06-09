"""Generated from Smithy shape ``com.amazonaws.ecs#CapacityProviderUpdateStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecs.errors import DeserializationError

CapacityProviderUpdateStatus: TypeAlias = Literal[
    "CREATE_IN_PROGRESS",
    "CREATE_COMPLETE",
    "CREATE_FAILED",
    "DELETE_IN_PROGRESS",
    "DELETE_COMPLETE",
    "DELETE_FAILED",
    "UPDATE_IN_PROGRESS",
    "UPDATE_COMPLETE",
    "UPDATE_FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATE_IN_PROGRESS",
        "CREATE_COMPLETE",
        "CREATE_FAILED",
        "DELETE_IN_PROGRESS",
        "DELETE_COMPLETE",
        "DELETE_FAILED",
        "UPDATE_IN_PROGRESS",
        "UPDATE_COMPLETE",
        "UPDATE_FAILED",
    )
)


def serialize_aws_json_1_1(value: CapacityProviderUpdateStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CapacityProviderUpdateStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CapacityProviderUpdateStatus value: {data!r}"
        )
    return cast(CapacityProviderUpdateStatus, data)
