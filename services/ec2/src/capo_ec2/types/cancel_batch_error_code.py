"""Generated from Smithy shape ``com.amazonaws.ec2#CancelBatchErrorCode``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

CancelBatchErrorCode: TypeAlias = Literal[
    "fleetRequestIdDoesNotExist",
    "fleetRequestIdMalformed",
    "fleetRequestNotInCancellableState",
    "unexpectedError",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: CancelBatchErrorCode) -> str:
    return value


def from_ec2_query_text(text: str) -> CancelBatchErrorCode:
    return cast(CancelBatchErrorCode, text)


def serialize_ec2_query(
    value: CancelBatchErrorCode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> CancelBatchErrorCode:
    return from_ec2_query_text(el.text or "")
