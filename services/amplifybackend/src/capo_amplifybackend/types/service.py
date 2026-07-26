"""Generated from Smithy shape ``com.amazonaws.amplifybackend#Service``."""

from typing import Literal, TypeAlias, cast

Service: TypeAlias = Literal["COGNITO",]


# --- restJson1 ser/de ---
def serialize_json(value: Service) -> str:
    return value


def deserialize_json(data: str) -> Service:
    return cast(Service, data)
