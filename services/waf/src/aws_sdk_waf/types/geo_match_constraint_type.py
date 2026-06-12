"""Generated from Smithy shape ``com.amazonaws.waf#GeoMatchConstraintType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_waf.errors import DeserializationError

GeoMatchConstraintType: TypeAlias = Literal["Country",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Country",))


def serialize_aws_json_1_1(value: GeoMatchConstraintType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GeoMatchConstraintType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GeoMatchConstraintType value: {data!r}")
    return cast(GeoMatchConstraintType, data)
