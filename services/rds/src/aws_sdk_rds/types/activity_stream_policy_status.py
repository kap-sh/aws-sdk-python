"""Generated from Smithy shape ``com.amazonaws.rds#ActivityStreamPolicyStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rds._protocol.xml import Element

ActivityStreamPolicyStatus: TypeAlias = Literal[
    "locked",
    "unlocked",
    "locking-policy",
    "unlocking-policy",
]


# --- awsQuery ser/de ---
def to_query_text(value: ActivityStreamPolicyStatus) -> str:
    return value


def from_query_text(text: str) -> ActivityStreamPolicyStatus:
    return cast(ActivityStreamPolicyStatus, text)


def serialize_query(
    value: ActivityStreamPolicyStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ActivityStreamPolicyStatus:
    return from_query_text(el.text or "")
