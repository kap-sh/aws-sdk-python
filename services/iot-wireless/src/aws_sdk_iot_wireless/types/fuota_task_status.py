"""Generated from Smithy shape ``com.amazonaws.iotwireless#FuotaTaskStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_wireless.errors import DeserializationError

"""<p>The status of a FUOTA task.</p>"""
FuotaTaskStatus: TypeAlias = Literal[
    "Pending",
    "FuotaSession_Waiting",
    "In_FuotaSession",
    "FuotaDone",
    "Delete_Waiting",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Pending",
        "FuotaSession_Waiting",
        "In_FuotaSession",
        "FuotaDone",
        "Delete_Waiting",
    )
)


def serialize_json(value: FuotaTaskStatus) -> str:
    return value


def deserialize_json(data: str) -> FuotaTaskStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FuotaTaskStatus value: {data!r}")
    return cast(FuotaTaskStatus, data)
