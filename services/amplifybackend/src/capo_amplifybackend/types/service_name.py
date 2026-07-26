"""Generated from Smithy shape ``com.amazonaws.amplifybackend#ServiceName``."""

from typing import Literal, TypeAlias, cast

ServiceName: TypeAlias = Literal["S3",]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceName) -> str:
    return value


def deserialize_json(data: str) -> ServiceName:
    return cast(ServiceName, data)
