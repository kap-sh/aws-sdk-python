"""Generated from Smithy shape ``com.amazonaws.securityagent#Provider``."""

from typing import Literal, TypeAlias, cast

"""<p>Third-party provider type.</p>"""
Provider: TypeAlias = Literal["GITHUB",]


# --- restJson1 ser/de ---
def serialize_json(value: Provider) -> str:
    return value


def deserialize_json(data: str) -> Provider:
    return cast(Provider, data)
