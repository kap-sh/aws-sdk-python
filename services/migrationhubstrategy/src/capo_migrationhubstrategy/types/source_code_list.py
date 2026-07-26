"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#SourceCodeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.source_code

SourceCodeList: TypeAlias = list[
    "capo_migrationhubstrategy.types.source_code.SourceCode"
]


# --- restJson1 ser/de ---
def serialize_json(value: SourceCodeList) -> list:
    import capo_migrationhubstrategy.types.source_code

    out: list = []
    for item in value:
        out.append(capo_migrationhubstrategy.types.source_code.serialize_json(item))
    return out


def deserialize_json(data: list) -> SourceCodeList:
    import capo_migrationhubstrategy.types.source_code

    out: SourceCodeList = []
    for item in data:
        out.append(capo_migrationhubstrategy.types.source_code.deserialize_json(item))
    return out
