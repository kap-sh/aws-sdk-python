"""Generated from Smithy shape ``com.amazonaws.ec2#ReportInstanceReasonCodes``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

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
def to_ec2_query_text(value: ReportInstanceReasonCodes) -> str:
    return value


def from_ec2_query_text(text: str) -> ReportInstanceReasonCodes:
    return cast(ReportInstanceReasonCodes, text)


def serialize_ec2_query(
    value: ReportInstanceReasonCodes, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ReportInstanceReasonCodes:
    return from_ec2_query_text(el.text or "")
