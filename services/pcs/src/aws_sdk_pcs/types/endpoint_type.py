"""Generated from Smithy shape ``com.amazonaws.pcs#EndpointType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pcs.errors import DeserializationError

EndpointType: TypeAlias = Literal[
    "SLURMCTLD",
    "SLURMDBD",
    "SLURMRESTD",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SLURMCTLD",
        "SLURMDBD",
        "SLURMRESTD",
    )
)


def serialize_aws_json_1_0(value: EndpointType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EndpointType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EndpointType value: {data!r}")
    return cast(EndpointType, data)
