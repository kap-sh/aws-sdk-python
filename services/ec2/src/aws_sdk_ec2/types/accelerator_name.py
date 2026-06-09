"""Generated from Smithy shape ``com.amazonaws.ec2#AcceleratorName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

AcceleratorName: TypeAlias = Literal[
    "a100",
    "inferentia",
    "k520",
    "k80",
    "m60",
    "radeon-pro-v520",
    "t4",
    "vu9p",
    "v100",
    "a10g",
    "h100",
    "t4g",
    "l40s",
    "l4",
    "gaudi-hl-205",
    "inferentia2",
    "trainium",
    "trainium2",
    "u30",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "a100",
        "inferentia",
        "k520",
        "k80",
        "m60",
        "radeon-pro-v520",
        "t4",
        "vu9p",
        "v100",
        "a10g",
        "h100",
        "t4g",
        "l40s",
        "l4",
        "gaudi-hl-205",
        "inferentia2",
        "trainium",
        "trainium2",
        "u30",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "a100",
        "inferentia",
        "k520",
        "k80",
        "m60",
        "radeon-pro-v520",
        "t4",
        "vu9p",
        "v100",
        "a10g",
        "h100",
        "t4g",
        "l40s",
        "l4",
        "gaudi-hl-205",
        "inferentia2",
        "trainium",
        "trainium2",
        "u30",
    )
)


def to_ec2_query_text(value: AcceleratorName) -> str:
    return value


def from_ec2_query_text(text: str) -> AcceleratorName:
    if text not in _VALUES:
        raise DeserializationError(f"unknown AcceleratorName value: {text!r}")
    return cast(AcceleratorName, text)


def serialize_ec2_query(
    value: AcceleratorName, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> AcceleratorName:
    return from_ec2_query_text(el.text or "")
