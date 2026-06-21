"""Generated from Smithy shape ``com.amazonaws.redshift#ScheduledActionFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_redshift._protocol.xml import Element

ScheduledActionFilterName: TypeAlias = Literal[
    "cluster-identifier",
    "iam-role",
]


# --- awsQuery ser/de ---
def to_query_text(value: ScheduledActionFilterName) -> str:
    return value


def from_query_text(text: str) -> ScheduledActionFilterName:
    return cast(ScheduledActionFilterName, text)


def serialize_query(
    value: ScheduledActionFilterName, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ScheduledActionFilterName:
    return from_query_text(el.text or "")
