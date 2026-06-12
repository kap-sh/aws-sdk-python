"""Generated from Smithy shape ``com.amazonaws.customerprofiles#IdentityResolutionJobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_customer_profiles.errors import DeserializationError

IdentityResolutionJobStatus: TypeAlias = Literal[
    "PENDING",
    "PREPROCESSING",
    "FIND_MATCHING",
    "MERGING",
    "COMPLETED",
    "PARTIAL_SUCCESS",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "PREPROCESSING",
        "FIND_MATCHING",
        "MERGING",
        "COMPLETED",
        "PARTIAL_SUCCESS",
        "FAILED",
    )
)


def serialize_json(value: IdentityResolutionJobStatus) -> str:
    return value


def deserialize_json(data: str) -> IdentityResolutionJobStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown IdentityResolutionJobStatus value: {data!r}"
        )
    return cast(IdentityResolutionJobStatus, data)
