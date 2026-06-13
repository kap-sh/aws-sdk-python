"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#GroupSharingPreferenceEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bcm_pricing_calculator.errors import DeserializationError

GroupSharingPreferenceEnum: TypeAlias = Literal[
    "OPEN",
    "PRIORITIZED",
    "RESTRICTED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OPEN",
        "PRIORITIZED",
        "RESTRICTED",
    )
)


def serialize_aws_json_1_0(value: GroupSharingPreferenceEnum) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> GroupSharingPreferenceEnum:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown GroupSharingPreferenceEnum value: {data!r}"
        )
    return cast(GroupSharingPreferenceEnum, data)
