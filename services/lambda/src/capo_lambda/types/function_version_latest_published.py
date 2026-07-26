"""Generated from Smithy shape ``com.amazonaws.lambda#FunctionVersionLatestPublished``."""

from typing import Literal, TypeAlias, cast

FunctionVersionLatestPublished: TypeAlias = Literal["LATEST_PUBLISHED",]


# --- restJson1 ser/de ---
def serialize_json(value: FunctionVersionLatestPublished) -> str:
    return value


def deserialize_json(data: str) -> FunctionVersionLatestPublished:
    return cast(FunctionVersionLatestPublished, data)
