"""Generated from Smithy shape ``com.amazonaws.appsync#RuntimeName``."""

from typing import Literal, TypeAlias, cast

RuntimeName: TypeAlias = Literal["APPSYNC_JS",]


# --- restJson1 ser/de ---
def serialize_json(value: RuntimeName) -> str:
    return value


def deserialize_json(data: str) -> RuntimeName:
    return cast(RuntimeName, data)
