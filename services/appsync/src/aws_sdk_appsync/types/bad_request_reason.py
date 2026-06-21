"""Generated from Smithy shape ``com.amazonaws.appsync#BadRequestReason``."""

from typing import Literal, TypeAlias, cast

"""<p>Provides context for the cause of the bad request. The only supported value is <code>CODE_ERROR</code>.</p>"""
BadRequestReason: TypeAlias = Literal["CODE_ERROR",]


# --- restJson1 ser/de ---
def serialize_json(value: BadRequestReason) -> str:
    return value


def deserialize_json(data: str) -> BadRequestReason:
    return cast(BadRequestReason, data)
