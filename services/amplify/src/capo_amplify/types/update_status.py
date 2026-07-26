"""Generated from Smithy shape ``com.amazonaws.amplify#UpdateStatus``."""

from typing import Literal, TypeAlias, cast

UpdateStatus: TypeAlias = Literal[
    "REQUESTING_CERTIFICATE",
    "PENDING_VERIFICATION",
    "IMPORTING_CUSTOM_CERTIFICATE",
    "PENDING_DEPLOYMENT",
    "AWAITING_APP_CNAME",
    "UPDATE_COMPLETE",
    "UPDATE_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateStatus) -> str:
    return value


def deserialize_json(data: str) -> UpdateStatus:
    return cast(UpdateStatus, data)
