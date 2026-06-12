"""Generated from Smithy shape ``com.amazonaws.acmpca#CrlType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_acm_pca.errors import DeserializationError

CrlType: TypeAlias = Literal[
    "COMPLETE",
    "PARTITIONED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COMPLETE",
        "PARTITIONED",
    )
)


def serialize_aws_json_1_1(value: CrlType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CrlType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CrlType value: {data!r}")
    return cast(CrlType, data)
