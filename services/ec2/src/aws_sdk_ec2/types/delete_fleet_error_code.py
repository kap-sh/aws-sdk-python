"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteFleetErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

DeleteFleetErrorCode: TypeAlias = Literal[
    "fleetIdDoesNotExist",
    "fleetIdMalformed",
    "fleetNotInDeletableState",
    "unexpectedError",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "fleetIdDoesNotExist",
        "fleetIdMalformed",
        "fleetNotInDeletableState",
        "unexpectedError",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "fleetIdDoesNotExist",
        "fleetIdMalformed",
        "fleetNotInDeletableState",
        "unexpectedError",
    )
)


def to_ec2_query_text(value: DeleteFleetErrorCode) -> str:
    return value


def from_ec2_query_text(text: str) -> DeleteFleetErrorCode:
    if text not in _VALUES:
        raise DeserializationError(f"unknown DeleteFleetErrorCode value: {text!r}")
    return cast(DeleteFleetErrorCode, text)


def serialize_ec2_query(
    value: DeleteFleetErrorCode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> DeleteFleetErrorCode:
    return from_ec2_query_text(el.text or "")
