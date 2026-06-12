"""Generated from Smithy shape ``com.amazonaws.resiliencehub#HaArchitecture``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehub.errors import DeserializationError

HaArchitecture: TypeAlias = Literal[
    "MultiSite",
    "WarmStandby",
    "PilotLight",
    "BackupAndRestore",
    "NoRecoveryPlan",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MultiSite",
        "WarmStandby",
        "PilotLight",
        "BackupAndRestore",
        "NoRecoveryPlan",
    )
)


def serialize_json(value: HaArchitecture) -> str:
    return value


def deserialize_json(data: str) -> HaArchitecture:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HaArchitecture value: {data!r}")
    return cast(HaArchitecture, data)
