"""Generated from Smithy shape ``com.amazonaws.sesv2#VerificationError``."""

from typing import Literal, TypeAlias, cast

VerificationError: TypeAlias = Literal[
    "SERVICE_ERROR",
    "DNS_SERVER_ERROR",
    "HOST_NOT_FOUND",
    "TYPE_NOT_FOUND",
    "INVALID_VALUE",
    "REPLICATION_ACCESS_DENIED",
    "REPLICATION_PRIMARY_NOT_FOUND",
    "REPLICATION_PRIMARY_BYO_DKIM_NOT_SUPPORTED",
    "REPLICATION_REPLICA_AS_PRIMARY_NOT_SUPPORTED",
    "REPLICATION_PRIMARY_INVALID_REGION",
]


# --- restJson1 ser/de ---
def serialize_json(value: VerificationError) -> str:
    return value


def deserialize_json(data: str) -> VerificationError:
    return cast(VerificationError, data)
