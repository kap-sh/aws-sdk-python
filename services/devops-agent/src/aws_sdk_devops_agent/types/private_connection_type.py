"""Generated from Smithy shape ``com.amazonaws.devopsagent#PrivateConnectionType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of Private Connection.</p>"""
PrivateConnectionType: TypeAlias = Literal[
    "SELF_MANAGED",
    "SERVICE_MANAGED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PrivateConnectionType) -> str:
    return value


def deserialize_json(data: str) -> PrivateConnectionType:
    return cast(PrivateConnectionType, data)
