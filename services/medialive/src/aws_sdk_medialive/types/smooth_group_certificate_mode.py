"""Generated from Smithy shape ``com.amazonaws.medialive#SmoothGroupCertificateMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Smooth Group Certificate Mode"""
SmoothGroupCertificateMode: TypeAlias = Literal[
    "SELF_SIGNED",
    "VERIFY_AUTHENTICITY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SELF_SIGNED",
        "VERIFY_AUTHENTICITY",
    )
)


def serialize_json(value: SmoothGroupCertificateMode) -> str:
    return value


def deserialize_json(data: str) -> SmoothGroupCertificateMode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SmoothGroupCertificateMode value: {data!r}"
        )
    return cast(SmoothGroupCertificateMode, data)
