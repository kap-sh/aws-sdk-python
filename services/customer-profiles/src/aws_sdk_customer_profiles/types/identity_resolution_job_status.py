"""Generated from Smithy shape ``com.amazonaws.customerprofiles#IdentityResolutionJobStatus``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: IdentityResolutionJobStatus) -> str:
    return value


def deserialize_json(data: str) -> IdentityResolutionJobStatus:
    return cast(IdentityResolutionJobStatus, data)
