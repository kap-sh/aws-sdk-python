"""Generated from Smithy shape ``com.amazonaws.acm#RenewalEligibility``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_acm.errors import DeserializationError

RenewalEligibility: TypeAlias = Literal[
    "ELIGIBLE",
    "INELIGIBLE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ELIGIBLE",
        "INELIGIBLE",
    )
)


def serialize_aws_json_1_1(value: RenewalEligibility) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RenewalEligibility:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RenewalEligibility value: {data!r}")
    return cast(RenewalEligibility, data)
