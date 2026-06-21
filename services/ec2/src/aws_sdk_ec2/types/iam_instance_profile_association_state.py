"""Generated from Smithy shape ``com.amazonaws.ec2#IamInstanceProfileAssociationState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

IamInstanceProfileAssociationState: TypeAlias = Literal[
    "associating",
    "associated",
    "disassociating",
    "disassociated",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: IamInstanceProfileAssociationState) -> str:
    return value


def from_ec2_query_text(text: str) -> IamInstanceProfileAssociationState:
    return cast(IamInstanceProfileAssociationState, text)


def serialize_ec2_query(
    value: IamInstanceProfileAssociationState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> IamInstanceProfileAssociationState:
    return from_ec2_query_text(el.text or "")
