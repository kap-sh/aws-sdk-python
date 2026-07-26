"""Generated from Smithy shape ``com.amazonaws.emrcontainers#EndpointState``."""

from typing import Literal, TypeAlias, cast

EndpointState: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "TERMINATING",
    "TERMINATED",
    "TERMINATED_WITH_ERRORS",
]


# --- restJson1 ser/de ---
def serialize_json(value: EndpointState) -> str:
    return value


def deserialize_json(data: str) -> EndpointState:
    return cast(EndpointState, data)
