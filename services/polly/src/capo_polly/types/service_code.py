"""Generated from Smithy shape ``com.amazonaws.polly#ServiceCode``."""

from typing import Literal, TypeAlias, cast

ServiceCode: TypeAlias = Literal["polly",]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceCode) -> str:
    return value


def deserialize_json(data: str) -> ServiceCode:
    return cast(ServiceCode, data)
