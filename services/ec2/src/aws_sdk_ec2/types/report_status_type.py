"""Generated from Smithy shape ``com.amazonaws.ec2#ReportStatusType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

ReportStatusType: TypeAlias = Literal[
    "ok",
    "impaired",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: ReportStatusType) -> str:
    return value


def from_ec2_query_text(text: str) -> ReportStatusType:
    return cast(ReportStatusType, text)


def serialize_ec2_query(
    value: ReportStatusType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ReportStatusType:
    return from_ec2_query_text(el.text or "")
