"""Generated from Smithy shape ``com.amazonaws.securityhub#FindingHistoryUpdateSourceType``."""

from typing import Literal, TypeAlias, cast

FindingHistoryUpdateSourceType: TypeAlias = Literal[
    "BATCH_UPDATE_FINDINGS",
    "BATCH_IMPORT_FINDINGS",
]


# --- restJson1 ser/de ---
def serialize_json(value: FindingHistoryUpdateSourceType) -> str:
    return value


def deserialize_json(data: str) -> FindingHistoryUpdateSourceType:
    return cast(FindingHistoryUpdateSourceType, data)
