"""Generated from Smithy shape ``com.amazonaws.eks#RepairAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_eks.errors import DeserializationError

RepairAction: TypeAlias = Literal[
    "Replace",
    "Reboot",
    "NoAction",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Replace",
        "Reboot",
        "NoAction",
    )
)


def serialize_json(value: RepairAction) -> str:
    return value


def deserialize_json(data: str) -> RepairAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RepairAction value: {data!r}")
    return cast(RepairAction, data)
