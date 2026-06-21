"""Generated from Smithy shape ``com.amazonaws.guardduty#DestinationType``."""

from typing import Literal, TypeAlias, cast

DestinationType: TypeAlias = Literal["S3",]


# --- restJson1 ser/de ---
def serialize_json(value: DestinationType) -> str:
    return value


def deserialize_json(data: str) -> DestinationType:
    return cast(DestinationType, data)
