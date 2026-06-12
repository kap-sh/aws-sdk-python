"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#RxNormEntityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_comprehendmedical.errors import DeserializationError

RxNormEntityType: TypeAlias = Literal[
    "BRAND_NAME",
    "GENERIC_NAME",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BRAND_NAME",
        "GENERIC_NAME",
    )
)


def serialize_aws_json_1_1(value: RxNormEntityType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RxNormEntityType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RxNormEntityType value: {data!r}")
    return cast(RxNormEntityType, data)
