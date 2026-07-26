"""Generated from Smithy shape ``com.amazonaws.s3outposts#EndpointAccessType``."""

from typing import Literal, TypeAlias, cast

EndpointAccessType: TypeAlias = Literal[
    "Private",
    "CustomerOwnedIp",
]


# --- restJson1 ser/de ---
def serialize_json(value: EndpointAccessType) -> str:
    return value


def deserialize_json(data: str) -> EndpointAccessType:
    return cast(EndpointAccessType, data)
