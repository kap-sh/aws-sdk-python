"""Generated from Smithy shape ``com.amazonaws.macie2#ErrorCode``."""

from typing import Literal, TypeAlias, cast

"""<p>The source of an issue or delay. Possible values are:</p>"""
ErrorCode: TypeAlias = Literal[
    "ClientError",
    "InternalError",
]


# --- restJson1 ser/de ---
def serialize_json(value: ErrorCode) -> str:
    return value


def deserialize_json(data: str) -> ErrorCode:
    return cast(ErrorCode, data)
