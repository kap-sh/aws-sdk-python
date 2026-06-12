"""Generated from Smithy shape ``com.amazonaws.wafv2#OversizeHandling``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wafv2.errors import DeserializationError

OversizeHandling: TypeAlias = Literal[
    "CONTINUE",
    "MATCH",
    "NO_MATCH",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CONTINUE",
        "MATCH",
        "NO_MATCH",
    )
)


def serialize_aws_json_1_1(value: OversizeHandling) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OversizeHandling:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OversizeHandling value: {data!r}")
    return cast(OversizeHandling, data)
