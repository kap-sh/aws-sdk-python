"""Generated from Smithy shape ``com.amazonaws.medialive#RtmpOutputCertificateMode``."""

from typing import Literal, TypeAlias, cast

"""Rtmp Output Certificate Mode"""
RtmpOutputCertificateMode: TypeAlias = Literal[
    "SELF_SIGNED",
    "VERIFY_AUTHENTICITY",
]


# --- restJson1 ser/de ---
def serialize_json(value: RtmpOutputCertificateMode) -> str:
    return value


def deserialize_json(data: str) -> RtmpOutputCertificateMode:
    return cast(RtmpOutputCertificateMode, data)
