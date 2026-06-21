"""Generated from Smithy shape ``com.amazonaws.wafregional#PredicateType``."""

from typing import Literal, TypeAlias, cast

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
def serialize_aws_json_1_1(value: PredicateType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PredicateType:
    return cast(PredicateType, data)
