"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#IsmEncryptionMethod``."""

from typing import Literal, TypeAlias, cast

IsmEncryptionMethod: TypeAlias = Literal["CENC",]


# --- restJson1 ser/de ---
def serialize_json(value: IsmEncryptionMethod) -> str:
    return value


def deserialize_json(data: str) -> IsmEncryptionMethod:
    return cast(IsmEncryptionMethod, data)
