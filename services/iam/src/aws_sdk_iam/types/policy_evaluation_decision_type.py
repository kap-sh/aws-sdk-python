"""Generated from Smithy shape ``com.amazonaws.iam#PolicyEvaluationDecisionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iam._protocol.xml import Element

PolicyEvaluationDecisionType: TypeAlias = Literal[
    "allowed",
    "explicitDeny",
    "implicitDeny",
]


# --- awsQuery ser/de ---
def to_query_text(value: PolicyEvaluationDecisionType) -> str:
    return value


def from_query_text(text: str) -> PolicyEvaluationDecisionType:
    return cast(PolicyEvaluationDecisionType, text)


def serialize_query(
    value: PolicyEvaluationDecisionType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> PolicyEvaluationDecisionType:
    return from_query_text(el.text or "")
