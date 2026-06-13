"""Generated from Smithy shape ``com.amazonaws.invoicing#ProcurementPortalPreferenceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_invoicing.errors import DeserializationError

ProcurementPortalPreferenceStatus: TypeAlias = Literal[
    "PENDING_VERIFICATION",
    "TEST_INITIALIZED",
    "TEST_INITIALIZATION_FAILED",
    "TEST_FAILED",
    "ACTIVE",
    "SUSPENDED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING_VERIFICATION",
        "TEST_INITIALIZED",
        "TEST_INITIALIZATION_FAILED",
        "TEST_FAILED",
        "ACTIVE",
        "SUSPENDED",
    )
)


def serialize_aws_json_1_0(value: ProcurementPortalPreferenceStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ProcurementPortalPreferenceStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ProcurementPortalPreferenceStatus value: {data!r}"
        )
    return cast(ProcurementPortalPreferenceStatus, data)
