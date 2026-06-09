"""Generated from Smithy shape ``com.amazonaws.ec2#UnsuccessfulInstanceCreditSpecificationErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

UnsuccessfulInstanceCreditSpecificationErrorCode: TypeAlias = Literal[
    "InvalidInstanceID.Malformed",
    "InvalidInstanceID.NotFound",
    "IncorrectInstanceState",
    "InstanceCreditSpecification.NotSupported",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InvalidInstanceID.Malformed",
        "InvalidInstanceID.NotFound",
        "IncorrectInstanceState",
        "InstanceCreditSpecification.NotSupported",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "InvalidInstanceID.Malformed",
        "InvalidInstanceID.NotFound",
        "IncorrectInstanceState",
        "InstanceCreditSpecification.NotSupported",
    )
)


def to_ec2_query_text(value: UnsuccessfulInstanceCreditSpecificationErrorCode) -> str:
    return value


def from_ec2_query_text(text: str) -> UnsuccessfulInstanceCreditSpecificationErrorCode:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown UnsuccessfulInstanceCreditSpecificationErrorCode value: {text!r}"
        )
    return cast(UnsuccessfulInstanceCreditSpecificationErrorCode, text)


def serialize_ec2_query(
    value: UnsuccessfulInstanceCreditSpecificationErrorCode,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(
    el: Element,
) -> UnsuccessfulInstanceCreditSpecificationErrorCode:
    return from_ec2_query_text(el.text or "")
