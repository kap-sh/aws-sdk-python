"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceRebootMigrationState``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

InstanceRebootMigrationState: TypeAlias = Literal[
    "disabled",
    "default",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "disabled",
        "default",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "disabled",
        "default",
    )
)


def to_ec2_query_text(value: InstanceRebootMigrationState) -> str:
    return value


def from_ec2_query_text(text: str) -> InstanceRebootMigrationState:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown InstanceRebootMigrationState value: {text!r}"
        )
    return cast(InstanceRebootMigrationState, text)


def serialize_ec2_query(
    value: InstanceRebootMigrationState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> InstanceRebootMigrationState:
    return from_ec2_query_text(el.text or "")
