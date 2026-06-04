"""Generated from Smithy shape ``com.amazonaws.iam#PolicyEvaluationDecisionType``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_iam.errors import DeserializationError
from aws_sdk_iam._protocol.xml import Element

PolicyEvaluationDecisionType: TypeAlias = Literal[
    "allowed",
    "explicitDeny",
    "implicitDeny",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "allowed",
        "explicitDeny",
        "implicitDeny",
    )
)


def to_query_text(value: PolicyEvaluationDecisionType) -> str:
    return value


def from_query_text(text: str) -> PolicyEvaluationDecisionType:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown PolicyEvaluationDecisionType value: {text!r}"
        )
    return cast(PolicyEvaluationDecisionType, text)


def serialize_query(
    value: PolicyEvaluationDecisionType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> PolicyEvaluationDecisionType:
    return from_query_text(el.text or "")
