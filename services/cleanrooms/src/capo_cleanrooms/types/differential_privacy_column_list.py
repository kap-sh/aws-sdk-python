"""Generated from Smithy shape ``com.amazonaws.cleanrooms#DifferentialPrivacyColumnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.differential_privacy_column

DifferentialPrivacyColumnList: TypeAlias = list[
    "capo_cleanrooms.types.differential_privacy_column.DifferentialPrivacyColumn"
]


# --- restJson1 ser/de ---
def serialize_json(value: DifferentialPrivacyColumnList) -> list:
    import capo_cleanrooms.types.differential_privacy_column

    out: list = []
    for item in value:
        out.append(
            capo_cleanrooms.types.differential_privacy_column.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DifferentialPrivacyColumnList:
    import capo_cleanrooms.types.differential_privacy_column

    out: DifferentialPrivacyColumnList = []
    for item in data:
        out.append(
            capo_cleanrooms.types.differential_privacy_column.deserialize_json(item)
        )
    return out
