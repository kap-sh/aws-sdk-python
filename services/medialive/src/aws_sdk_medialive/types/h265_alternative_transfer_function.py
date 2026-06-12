"""Generated from Smithy shape ``com.amazonaws.medialive#H265AlternativeTransferFunction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""H265 Alternative Transfer Function"""
H265AlternativeTransferFunction: TypeAlias = Literal[
    "INSERT",
    "OMIT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INSERT",
        "OMIT",
    )
)


def serialize_json(value: H265AlternativeTransferFunction) -> str:
    return value


def deserialize_json(data: str) -> H265AlternativeTransferFunction:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown H265AlternativeTransferFunction value: {data!r}"
        )
    return cast(H265AlternativeTransferFunction, data)
