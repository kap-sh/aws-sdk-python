"""Generated from Smithy shape ``com.amazonaws.ses#VerificationTokenList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ses._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ses.types.verification_token

VerificationTokenList: TypeAlias = list[
    "aws_sdk_ses.types.verification_token.VerificationToken"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: VerificationTokenList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.member.{n}", str(item)))


def deserialize_query(el: Element) -> VerificationTokenList:
    out: VerificationTokenList = []
    for child in el.findall("member"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: VerificationTokenList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> VerificationTokenList:
    out: VerificationTokenList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
