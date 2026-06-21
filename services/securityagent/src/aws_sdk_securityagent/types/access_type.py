"""Generated from Smithy shape ``com.amazonaws.securityagent#AccessType``."""

from typing import Literal, TypeAlias, cast

"""<p>Defines the visibility level of provider resources. PRIVATE indicates restricted access, while PUBLIC indicates open access.</p>"""
AccessType: TypeAlias = Literal[
    "PRIVATE",
    "PUBLIC",
]


# --- restJson1 ser/de ---
def serialize_json(value: AccessType) -> str:
    return value


def deserialize_json(data: str) -> AccessType:
    return cast(AccessType, data)
