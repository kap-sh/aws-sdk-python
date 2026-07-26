"""Generated from Smithy shape ``com.amazonaws.guardduty#FindingStatisticType``."""

from typing import Literal, TypeAlias, cast

FindingStatisticType: TypeAlias = Literal["COUNT_BY_SEVERITY",]


# --- restJson1 ser/de ---
def serialize_json(value: FindingStatisticType) -> str:
    return value


def deserialize_json(data: str) -> FindingStatisticType:
    return cast(FindingStatisticType, data)
