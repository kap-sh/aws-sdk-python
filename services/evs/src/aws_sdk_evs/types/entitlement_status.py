"""Generated from Smithy shape ``com.amazonaws.evs#EntitlementStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_evs.errors import DeserializationError

EntitlementStatus: TypeAlias = Literal[
    "CREATING",
    "CREATED",
    "DELETED",
    "AT_RISK",
    "ENTITLEMENT_REMOVED",
    "CREATE_FAILED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "CREATED",
        "DELETED",
        "AT_RISK",
        "ENTITLEMENT_REMOVED",
        "CREATE_FAILED",
    )
)


def serialize_aws_json_1_0(value: EntitlementStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EntitlementStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EntitlementStatus value: {data!r}")
    return cast(EntitlementStatus, data)
