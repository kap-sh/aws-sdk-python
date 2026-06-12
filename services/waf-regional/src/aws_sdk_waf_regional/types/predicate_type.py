"""Generated from Smithy shape ``com.amazonaws.wafregional#PredicateType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_waf_regional.errors import DeserializationError

PredicateType: TypeAlias = Literal[
    "IPMatch",
    "ByteMatch",
    "SqlInjectionMatch",
    "GeoMatch",
    "SizeConstraint",
    "XssMatch",
    "RegexMatch",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IPMatch",
        "ByteMatch",
        "SqlInjectionMatch",
        "GeoMatch",
        "SizeConstraint",
        "XssMatch",
        "RegexMatch",
    )
)


def serialize_aws_json_1_1(value: PredicateType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PredicateType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PredicateType value: {data!r}")
    return cast(PredicateType, data)
