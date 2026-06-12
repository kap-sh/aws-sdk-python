"""Generated from Smithy shape ``com.amazonaws.route53domains#SortOrder``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route_53_domains.errors import DeserializationError

SortOrder: TypeAlias = Literal[
    "ASC",
    "DESC",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASC",
        "DESC",
    )
)


def serialize_aws_json_1_1(value: SortOrder) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SortOrder:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SortOrder value: {data!r}")
    return cast(SortOrder, data)
