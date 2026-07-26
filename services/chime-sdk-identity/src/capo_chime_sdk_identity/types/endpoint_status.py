"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#EndpointStatus``."""

from typing import Literal, TypeAlias, cast

EndpointStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: EndpointStatus) -> str:
    return value


def deserialize_json(data: str) -> EndpointStatus:
    return cast(EndpointStatus, data)
