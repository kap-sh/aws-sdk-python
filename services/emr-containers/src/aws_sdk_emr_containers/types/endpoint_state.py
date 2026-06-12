"""Generated from Smithy shape ``com.amazonaws.emrcontainers#EndpointState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_emr_containers.errors import DeserializationError

EndpointState: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "TERMINATING",
    "TERMINATED",
    "TERMINATED_WITH_ERRORS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "ACTIVE",
        "TERMINATING",
        "TERMINATED",
        "TERMINATED_WITH_ERRORS",
    )
)


def serialize_json(value: EndpointState) -> str:
    return value


def deserialize_json(data: str) -> EndpointState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EndpointState value: {data!r}")
    return cast(EndpointState, data)
