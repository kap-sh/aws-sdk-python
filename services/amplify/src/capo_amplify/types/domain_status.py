"""Generated from Smithy shape ``com.amazonaws.amplify#DomainStatus``."""

from typing import Literal, TypeAlias, cast

DomainStatus: TypeAlias = Literal[
    "PENDING_VERIFICATION",
    "IN_PROGRESS",
    "AVAILABLE",
    "IMPORTING_CUSTOM_CERTIFICATE",
    "PENDING_DEPLOYMENT",
    "AWAITING_APP_CNAME",
    "FAILED",
    "CREATING",
    "REQUESTING_CERTIFICATE",
    "UPDATING",
]


# --- restJson1 ser/de ---
def serialize_json(value: DomainStatus) -> str:
    return value


def deserialize_json(data: str) -> DomainStatus:
    return cast(DomainStatus, data)
