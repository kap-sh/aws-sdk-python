"""Generated from Smithy shape ``com.amazonaws.rds#TargetType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rds._protocol.xml import Element

TargetType: TypeAlias = Literal[
    "RDS_INSTANCE",
    "RDS_SERVERLESS_ENDPOINT",
    "TRACKED_CLUSTER",
]


# --- awsQuery ser/de ---
def to_query_text(value: TargetType) -> str:
    return value


def from_query_text(text: str) -> TargetType:
    return cast(TargetType, text)


def serialize_query(
    value: TargetType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> TargetType:
    return from_query_text(el.text or "")
