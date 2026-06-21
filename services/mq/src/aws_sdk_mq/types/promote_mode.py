"""Generated from Smithy shape ``com.amazonaws.mq#PromoteMode``."""

from typing import Literal, TypeAlias, cast

"""<p>The Promote mode requested.</p>"""
PromoteMode: TypeAlias = Literal[
    "SWITCHOVER",
    "FAILOVER",
]


# --- restJson1 ser/de ---
def serialize_json(value: PromoteMode) -> str:
    return value


def deserialize_json(data: str) -> PromoteMode:
    return cast(PromoteMode, data)
