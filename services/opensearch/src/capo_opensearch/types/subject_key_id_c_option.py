"""Generated from Smithy shape ``com.amazonaws.opensearch#SubjectKeyIdCOption``."""

from typing import Literal, TypeAlias, cast

SubjectKeyIdCOption: TypeAlias = Literal[
    "UserName",
    "UserId",
    "Email",
]


# --- restJson1 ser/de ---
def serialize_json(value: SubjectKeyIdCOption) -> str:
    return value


def deserialize_json(data: str) -> SubjectKeyIdCOption:
    return cast(SubjectKeyIdCOption, data)
