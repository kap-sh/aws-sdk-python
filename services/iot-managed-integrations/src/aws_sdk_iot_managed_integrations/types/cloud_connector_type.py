"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#CloudConnectorType``."""

from typing import Literal, TypeAlias, cast

CloudConnectorType: TypeAlias = Literal[
    "LISTED",
    "UNLISTED",
]


# --- restJson1 ser/de ---
def serialize_json(value: CloudConnectorType) -> str:
    return value


def deserialize_json(data: str) -> CloudConnectorType:
    return cast(CloudConnectorType, data)
