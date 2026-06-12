"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#RxNormEntityCategory``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_comprehendmedical.errors import DeserializationError

RxNormEntityCategory: TypeAlias = Literal["MEDICATION",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("MEDICATION",))


def serialize_aws_json_1_1(value: RxNormEntityCategory) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RxNormEntityCategory:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RxNormEntityCategory value: {data!r}")
    return cast(RxNormEntityCategory, data)
