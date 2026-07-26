"""Generated from Smithy shape ``com.amazonaws.appfabric#AppAuthorizationStatus``."""

from typing import Literal, TypeAlias, cast

AppAuthorizationStatus: TypeAlias = Literal[
    "PendingConnect",
    "Connected",
    "ConnectionValidationFailed",
    "TokenAutoRotationFailed",
]


# --- restJson1 ser/de ---
def serialize_json(value: AppAuthorizationStatus) -> str:
    return value


def deserialize_json(data: str) -> AppAuthorizationStatus:
    return cast(AppAuthorizationStatus, data)
