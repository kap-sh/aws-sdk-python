"""Generated from Smithy shape ``com.amazonaws.tnb#UpdateSolNetworkType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_tnb.errors import DeserializationError

UpdateSolNetworkType: TypeAlias = Literal[
    "MODIFY_VNF_INFORMATION",
    "UPDATE_NS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MODIFY_VNF_INFORMATION",
        "UPDATE_NS",
    )
)


def serialize_json(value: UpdateSolNetworkType) -> str:
    return value


def deserialize_json(data: str) -> UpdateSolNetworkType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UpdateSolNetworkType value: {data!r}")
    return cast(UpdateSolNetworkType, data)
