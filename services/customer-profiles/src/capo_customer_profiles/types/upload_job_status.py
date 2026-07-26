"""Generated from Smithy shape ``com.amazonaws.customerprofiles#UploadJobStatus``."""

from typing import Literal, TypeAlias, cast

UploadJobStatus: TypeAlias = Literal[
    "CREATED",
    "IN_PROGRESS",
    "PARTIALLY_SUCCEEDED",
    "SUCCEEDED",
    "FAILED",
    "STOPPED",
]


# --- restJson1 ser/de ---
def serialize_json(value: UploadJobStatus) -> str:
    return value


def deserialize_json(data: str) -> UploadJobStatus:
    return cast(UploadJobStatus, data)
