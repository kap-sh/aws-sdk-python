"""Generated from Smithy shape ``com.amazonaws.devopsguru#OptInStatus``."""

from typing import Literal, TypeAlias, cast

"""<p> Specifies if DevOps Guru is enabled to create an Amazon Web Services Systems Manager OpsItem for each created insight. </p>"""
OptInStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: OptInStatus) -> str:
    return value


def deserialize_json(data: str) -> OptInStatus:
    return cast(OptInStatus, data)
