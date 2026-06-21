"""Generated from Smithy shape ``com.amazonaws.qbusiness#APISchemaType``."""

from typing import Literal, TypeAlias, cast

APISchemaType: TypeAlias = Literal["OPEN_API_V3",]


# --- restJson1 ser/de ---
def serialize_json(value: APISchemaType) -> str:
    return value


def deserialize_json(data: str) -> APISchemaType:
    return cast(APISchemaType, data)
