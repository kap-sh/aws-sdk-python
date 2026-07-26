"""Generated from Smithy shape ``com.amazonaws.apigateway#DomainNameStatus``."""

from typing import Literal, TypeAlias, cast

DomainNameStatus: TypeAlias = Literal[
    "AVAILABLE",
    "UPDATING",
    "PENDING",
    "PENDING_CERTIFICATE_REIMPORT",
    "PENDING_OWNERSHIP_VERIFICATION",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DomainNameStatus) -> str:
    return value


def deserialize_json(data: str) -> DomainNameStatus:
    return cast(DomainNameStatus, data)
