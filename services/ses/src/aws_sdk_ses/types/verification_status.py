"""Generated from Smithy shape ``com.amazonaws.ses#VerificationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ses._protocol.xml import Element

VerificationStatus: TypeAlias = Literal[
    "Pending",
    "Success",
    "Failed",
    "TemporaryFailure",
    "NotStarted",
]


# --- awsQuery ser/de ---
def to_query_text(value: VerificationStatus) -> str:
    return value


def from_query_text(text: str) -> VerificationStatus:
    return cast(VerificationStatus, text)


def serialize_query(
    value: VerificationStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> VerificationStatus:
    return from_query_text(el.text or "")
