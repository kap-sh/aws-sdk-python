"""Generated from Smithy shape ``com.amazonaws.ec2#VolumeStatusInfoStatus``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

VolumeStatusInfoStatus: TypeAlias = Literal[
    "ok",
    "impaired",
    "insufficient-data",
    "warning",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ok",
        "impaired",
        "insufficient-data",
        "warning",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "ok",
        "impaired",
        "insufficient-data",
        "warning",
    )
)


def to_ec2_query_text(value: VolumeStatusInfoStatus) -> str:
    return value


def from_ec2_query_text(text: str) -> VolumeStatusInfoStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown VolumeStatusInfoStatus value: {text!r}")
    return cast(VolumeStatusInfoStatus, text)


def serialize_ec2_query(
    value: VolumeStatusInfoStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> VolumeStatusInfoStatus:
    return from_ec2_query_text(el.text or "")
