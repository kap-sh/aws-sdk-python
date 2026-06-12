"""Generated from Smithy shape ``com.amazonaws.medialive#RtmpOutputCertificateMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Rtmp Output Certificate Mode"""
RtmpOutputCertificateMode: TypeAlias = Literal[
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


def serialize_json(value: RtmpOutputCertificateMode) -> str:
    return value


def deserialize_json(data: str) -> RtmpOutputCertificateMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RtmpOutputCertificateMode value: {data!r}")
    return cast(RtmpOutputCertificateMode, data)
