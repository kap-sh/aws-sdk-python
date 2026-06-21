"""Generated from Smithy shape ``com.amazonaws.qbusiness#ResponseConfigurationType``."""

from typing import Literal, TypeAlias, cast

ResponseConfigurationType: TypeAlias = Literal["ALL",]


# --- restJson1 ser/de ---
def serialize_json(value: ResponseConfigurationType) -> str:
    return value


def deserialize_json(data: str) -> ResponseConfigurationType:
    return cast(ResponseConfigurationType, data)
