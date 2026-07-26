"""Generated from Smithy shape ``com.amazonaws.guardduty#ScanCriterionKey``."""

from typing import Literal, TypeAlias, cast

"""<p>An enum value representing possible resource properties to match with given scan condition.</p>"""
ScanCriterionKey: TypeAlias = Literal["EC2_INSTANCE_TAG",]


# --- restJson1 ser/de ---
def serialize_json(value: ScanCriterionKey) -> str:
    return value


def deserialize_json(data: str) -> ScanCriterionKey:
    return cast(ScanCriterionKey, data)
