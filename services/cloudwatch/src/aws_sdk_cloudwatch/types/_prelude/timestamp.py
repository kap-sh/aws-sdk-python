"""Generated from Smithy prelude shape ``smithy.api#Timestamp``."""

import datetime

from aws_sdk_cloudwatch._protocol.xml import Element


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: datetime.datetime) -> float:
    return value.timestamp()


def deserialize_aws_json_1_0(data: float) -> datetime.datetime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)


# --- awsQuery ser/de ---
def to_query_text(value: datetime.datetime) -> str:
    return value.isoformat()


def from_query_text(text: str) -> datetime.datetime:
    return datetime.datetime.fromisoformat(text.replace("Z", "+00:00"))


def serialize_query(
    value: datetime.datetime, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> datetime.datetime:
    return from_query_text(el.text or "")
