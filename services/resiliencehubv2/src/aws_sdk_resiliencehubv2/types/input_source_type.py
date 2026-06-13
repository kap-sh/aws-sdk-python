"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#InputSourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehubv2.errors import DeserializationError

InputSourceType: TypeAlias = Literal[
    "CFN_STACK",
    "TAGS",
    "EKS",
    "TERRAFORM",
    "DESIGN_FILE",
    "MONITORING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CFN_STACK",
        "TAGS",
        "EKS",
        "TERRAFORM",
        "DESIGN_FILE",
        "MONITORING",
    )
)


def serialize_json(value: InputSourceType) -> str:
    return value


def deserialize_json(data: str) -> InputSourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InputSourceType value: {data!r}")
    return cast(InputSourceType, data)
