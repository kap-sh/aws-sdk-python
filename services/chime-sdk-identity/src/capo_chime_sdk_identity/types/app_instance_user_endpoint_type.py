"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#AppInstanceUserEndpointType``."""

from typing import Literal, TypeAlias, cast

AppInstanceUserEndpointType: TypeAlias = Literal[
    "APNS",
    "APNS_SANDBOX",
    "GCM",
]


# --- restJson1 ser/de ---
def serialize_json(value: AppInstanceUserEndpointType) -> str:
    return value


def deserialize_json(data: str) -> AppInstanceUserEndpointType:
    return cast(AppInstanceUserEndpointType, data)
