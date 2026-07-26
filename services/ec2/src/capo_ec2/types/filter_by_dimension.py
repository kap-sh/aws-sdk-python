"""Generated from Smithy shape ``com.amazonaws.ec2#FilterByDimension``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

FilterByDimension: TypeAlias = Literal[
    "resource-region",
    "availability-zone-id",
    "account-id",
    "account-name",
    "instance-family",
    "instance-type",
    "instance-platform",
    "reservation-arn",
    "reservation-id",
    "reservation-type",
    "reservation-create-timestamp",
    "reservation-start-timestamp",
    "reservation-end-timestamp",
    "reservation-end-date-type",
    "tenancy",
    "reservation-state",
    "reservation-instance-match-criteria",
    "reservation-unused-financial-owner",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: FilterByDimension) -> str:
    return value


def from_ec2_query_text(text: str) -> FilterByDimension:
    return cast(FilterByDimension, text)


def serialize_ec2_query(
    value: FilterByDimension, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> FilterByDimension:
    return from_ec2_query_text(el.text or "")
