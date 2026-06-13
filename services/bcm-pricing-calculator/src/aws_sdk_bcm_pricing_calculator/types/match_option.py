"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#MatchOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bcm_pricing_calculator.errors import DeserializationError

MatchOption: TypeAlias = Literal[
    "EQUALS",
    "STARTS_WITH",
    "CONTAINS",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EQUALS",
        "STARTS_WITH",
        "CONTAINS",
    )
)


def serialize_aws_json_1_0(value: MatchOption) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> MatchOption:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MatchOption value: {data!r}")
    return cast(MatchOption, data)
