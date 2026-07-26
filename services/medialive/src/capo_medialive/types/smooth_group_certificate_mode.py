"""Generated from Smithy shape ``com.amazonaws.medialive#SmoothGroupCertificateMode``."""

from typing import Literal, TypeAlias, cast

"""Smooth Group Certificate Mode"""
SmoothGroupCertificateMode: TypeAlias = Literal[
    "SELF_SIGNED",
    "VERIFY_AUTHENTICITY",
]


# --- restJson1 ser/de ---
def serialize_json(value: SmoothGroupCertificateMode) -> str:
    return value


def deserialize_json(data: str) -> SmoothGroupCertificateMode:
    return cast(SmoothGroupCertificateMode, data)
