"""Generated from Smithy shape ``com.amazonaws.datazone#HyperPodOrchestrator``."""

from typing import Literal, TypeAlias, cast

HyperPodOrchestrator: TypeAlias = Literal[
    "EKS",
    "SLURM",
]


# --- restJson1 ser/de ---
def serialize_json(value: HyperPodOrchestrator) -> str:
    return value


def deserialize_json(data: str) -> HyperPodOrchestrator:
    return cast(HyperPodOrchestrator, data)
