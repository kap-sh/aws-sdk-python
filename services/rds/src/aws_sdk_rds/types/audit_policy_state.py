"""Generated from Smithy shape ``com.amazonaws.rds#AuditPolicyState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rds._protocol.xml import Element

AuditPolicyState: TypeAlias = Literal[
    "locked",
    "unlocked",
]


# --- awsQuery ser/de ---
def to_query_text(value: AuditPolicyState) -> str:
    return value


def from_query_text(text: str) -> AuditPolicyState:
    return cast(AuditPolicyState, text)


def serialize_query(
    value: AuditPolicyState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> AuditPolicyState:
    return from_query_text(el.text or "")
