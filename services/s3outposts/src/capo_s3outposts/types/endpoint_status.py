"""Generated from Smithy shape ``com.amazonaws.s3outposts#EndpointStatus``."""

from typing import Literal, TypeAlias, cast

EndpointStatus: TypeAlias = Literal[
    "Pending",
    "Available",
    "Deleting",
    "Create_Failed",
    "Delete_Failed",
]


# --- restJson1 ser/de ---
def serialize_json(value: EndpointStatus) -> str:
    return value


def deserialize_json(data: str) -> EndpointStatus:
    return cast(EndpointStatus, data)
