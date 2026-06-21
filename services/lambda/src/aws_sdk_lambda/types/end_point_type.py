"""Generated from Smithy shape ``com.amazonaws.lambda#EndPointType``."""

from typing import Literal, TypeAlias, cast

EndPointType: TypeAlias = Literal["KAFKA_BOOTSTRAP_SERVERS",]


# --- restJson1 ser/de ---
def serialize_json(value: EndPointType) -> str:
    return value


def deserialize_json(data: str) -> EndPointType:
    return cast(EndPointType, data)
