"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DescribePortfolioShareType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_service_catalog.errors import DeserializationError

DescribePortfolioShareType: TypeAlias = Literal[
    "ACCOUNT",
    "ORGANIZATION",
    "ORGANIZATIONAL_UNIT",
    "ORGANIZATION_MEMBER_ACCOUNT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACCOUNT",
        "ORGANIZATION",
        "ORGANIZATIONAL_UNIT",
        "ORGANIZATION_MEMBER_ACCOUNT",
    )
)


def serialize_aws_json_1_1(value: DescribePortfolioShareType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DescribePortfolioShareType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DescribePortfolioShareType value: {data!r}"
        )
    return cast(DescribePortfolioShareType, data)
