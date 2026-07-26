"""Generated from Smithy shape ``com.amazonaws.s3files#ImportTrigger``."""

from typing import Literal, TypeAlias, cast

ImportTrigger: TypeAlias = Literal[
    "ON_DIRECTORY_FIRST_ACCESS",
    "ON_FILE_ACCESS",
]


# --- restJson1 ser/de ---
def serialize_json(value: ImportTrigger) -> str:
    return value


def deserialize_json(data: str) -> ImportTrigger:
    return cast(ImportTrigger, data)
