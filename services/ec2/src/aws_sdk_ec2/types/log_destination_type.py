"""Generated from Smithy shape ``com.amazonaws.ec2#LogDestinationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

LogDestinationType: TypeAlias = Literal[
    "cloud-watch-logs",
    "s3",
    "kinesis-data-firehose",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: LogDestinationType) -> str:
    return value


def from_ec2_query_text(text: str) -> LogDestinationType:
    return cast(LogDestinationType, text)


def serialize_ec2_query(
    value: LogDestinationType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> LogDestinationType:
    return from_ec2_query_text(el.text or "")
