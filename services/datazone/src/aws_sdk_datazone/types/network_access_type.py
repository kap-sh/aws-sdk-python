"""Generated from Smithy shape ``com.amazonaws.datazone#NetworkAccessType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

"""<p>The network access type for a notebook run in Amazon SageMaker Unified Studio.</p>"""
NetworkAccessType: TypeAlias = Literal[
    "PUBLIC_INTERNET_ONLY",
    "VPC_ONLY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PUBLIC_INTERNET_ONLY",
        "VPC_ONLY",
    )
)


def serialize_json(value: NetworkAccessType) -> str:
    return value


def deserialize_json(data: str) -> NetworkAccessType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NetworkAccessType value: {data!r}")
    return cast(NetworkAccessType, data)
