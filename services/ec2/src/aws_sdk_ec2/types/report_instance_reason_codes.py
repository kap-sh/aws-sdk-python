"""Generated from Smithy shape ``com.amazonaws.ec2#ReportInstanceReasonCodes``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

ReportInstanceReasonCodes: TypeAlias = Literal[
    "instance-stuck-in-state",
    "unresponsive",
    "not-accepting-credentials",
    "password-not-available",
    "performance-network",
    "performance-instance-store",
    "performance-ebs-volume",
    "performance-other",
    "other",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "instance-stuck-in-state",
        "unresponsive",
        "not-accepting-credentials",
        "password-not-available",
        "performance-network",
        "performance-instance-store",
        "performance-ebs-volume",
        "performance-other",
        "other",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "instance-stuck-in-state",
        "unresponsive",
        "not-accepting-credentials",
        "password-not-available",
        "performance-network",
        "performance-instance-store",
        "performance-ebs-volume",
        "performance-other",
        "other",
    )
)


def to_ec2_query_text(value: ReportInstanceReasonCodes) -> str:
    return value


def from_ec2_query_text(text: str) -> ReportInstanceReasonCodes:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ReportInstanceReasonCodes value: {text!r}")
    return cast(ReportInstanceReasonCodes, text)


def serialize_ec2_query(
    value: ReportInstanceReasonCodes, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ReportInstanceReasonCodes:
    return from_ec2_query_text(el.text or "")
