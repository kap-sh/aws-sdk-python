"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#RxNormTraitName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_comprehendmedical.errors import DeserializationError

RxNormTraitName: TypeAlias = Literal[
    "NEGATION",
    "PAST_HISTORY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NEGATION",
        "PAST_HISTORY",
    )
)


def serialize_aws_json_1_1(value: RxNormTraitName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RxNormTraitName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RxNormTraitName value: {data!r}")
    return cast(RxNormTraitName, data)
