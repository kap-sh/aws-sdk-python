"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityReservationInstancePlatform``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

CapacityReservationInstancePlatform: TypeAlias = Literal[
    "Linux/UNIX",
    "Red Hat Enterprise Linux",
    "SUSE Linux",
    "Windows",
    "Windows with SQL Server",
    "Windows with SQL Server Enterprise",
    "Windows with SQL Server Standard",
    "Windows with SQL Server Web",
    "Linux with SQL Server Standard",
    "Linux with SQL Server Web",
    "Linux with SQL Server Enterprise",
    "RHEL with SQL Server Standard",
    "RHEL with SQL Server Enterprise",
    "RHEL with SQL Server Web",
    "RHEL with HA",
    "RHEL with HA and SQL Server Standard",
    "RHEL with HA and SQL Server Enterprise",
    "Ubuntu Pro",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: CapacityReservationInstancePlatform) -> str:
    return value


def from_ec2_query_text(text: str) -> CapacityReservationInstancePlatform:
    return cast(CapacityReservationInstancePlatform, text)


def serialize_ec2_query(
    value: CapacityReservationInstancePlatform,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> CapacityReservationInstancePlatform:
    return from_ec2_query_text(el.text or "")
