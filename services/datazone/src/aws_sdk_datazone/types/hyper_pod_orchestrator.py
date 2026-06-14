"""Generated from Smithy shape ``com.amazonaws.datazone#HyperPodOrchestrator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

HyperPodOrchestrator: TypeAlias = Literal[
    "EKS",
    "SLURM",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EKS",
        "SLURM",
    )
)


def serialize_json(value: HyperPodOrchestrator) -> str:
    return value


def deserialize_json(data: str) -> HyperPodOrchestrator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HyperPodOrchestrator value: {data!r}")
    return cast(HyperPodOrchestrator, data)
