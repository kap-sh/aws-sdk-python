"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#CredentialLockerCreatedAt``."""

import datetime
from typing import TypeAlias

CredentialLockerCreatedAt: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: CredentialLockerCreatedAt) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> CredentialLockerCreatedAt:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
