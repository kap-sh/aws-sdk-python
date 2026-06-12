"""Generated from Smithy shape ``com.amazonaws.guardduty#ScanCriterionKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_guardduty.errors import DeserializationError

"""<p>An enum value representing possible resource properties to match with given scan condition.</p>"""
ScanCriterionKey: TypeAlias = Literal["EC2_INSTANCE_TAG",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("EC2_INSTANCE_TAG",))


def serialize_json(value: ScanCriterionKey) -> str:
    return value


def deserialize_json(data: str) -> ScanCriterionKey:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScanCriterionKey value: {data!r}")
    return cast(ScanCriterionKey, data)
