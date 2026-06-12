"""Generated from Smithy shape ``com.amazonaws.servicecatalog#PortfolioShareType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_service_catalog.errors import DeserializationError

PortfolioShareType: TypeAlias = Literal[
    "IMPORTED",
    "AWS_SERVICECATALOG",
    "AWS_ORGANIZATIONS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IMPORTED",
        "AWS_SERVICECATALOG",
        "AWS_ORGANIZATIONS",
    )
)


def serialize_aws_json_1_1(value: PortfolioShareType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PortfolioShareType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PortfolioShareType value: {data!r}")
    return cast(PortfolioShareType, data)
