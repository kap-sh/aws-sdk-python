"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteQueuedReservedInstancesErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

DeleteQueuedReservedInstancesErrorCode: TypeAlias = Literal[
    "reserved-instances-id-invalid",
    "reserved-instances-not-in-queued-state",
    "unexpected-error",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "reserved-instances-id-invalid",
        "reserved-instances-not-in-queued-state",
        "unexpected-error",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "reserved-instances-id-invalid",
        "reserved-instances-not-in-queued-state",
        "unexpected-error",
    )
)


def to_ec2_query_text(value: DeleteQueuedReservedInstancesErrorCode) -> str:
    return value


def from_ec2_query_text(text: str) -> DeleteQueuedReservedInstancesErrorCode:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown DeleteQueuedReservedInstancesErrorCode value: {text!r}"
        )
    return cast(DeleteQueuedReservedInstancesErrorCode, text)


def serialize_ec2_query(
    value: DeleteQueuedReservedInstancesErrorCode,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> DeleteQueuedReservedInstancesErrorCode:
    return from_ec2_query_text(el.text or "")
